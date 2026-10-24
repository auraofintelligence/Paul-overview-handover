"""Check local Wiki source and prepare a bundle for explicit publication."""
from pathlib import Path
import hashlib
import json
import re

root = Path(__file__).resolve().parents[1]
wiki = root / 'wiki'
base = 'https://github.com/auraofintelligence/Paul-overview-handover/wiki/'
manifest = json.loads((wiki / 'page-order.json').read_text())
slugs = {item['slug'] for item in manifest}
pages = []
for item in manifest:
    content = (wiki / (item['slug'] + '.md')).read_text()
    if not content.strip():
        raise ValueError('Empty page: ' + item['slug'])
    pages.append({**item, 'content': content})
source = next(page['content'] for page in pages if page['slug'] == 'Sources-and-documents')
public_ids = set(re.findall(r'^### (S\d\d)$', source, re.M))
document_ids = set(re.findall(r'^\| (D\d\d) \|', source, re.M))
for page in pages:
    content = page['content']
    targets = set(re.findall(re.escape(base) + r'([^\s)#]+)', content))
    if targets - slugs:
        raise ValueError(f"Unknown Wiki target in {page['slug']}: {targets - slugs}")
    if set(re.findall(r'\[(S\d\d)\]', content)) - public_ids:
        raise ValueError('Unknown public source in ' + page['slug'])
    if set(re.findall(r'\[(D\d\d)\]', content)) - document_ids:
        raise ValueError('Unknown background document in ' + page['slug'])
    if re.search(r'\[\[|\]\]|genui|filecite', content):
        raise ValueError('Unresolved authoring markup in ' + page['slug'])
(wiki / 'publish-bundle.json').write_text(json.dumps(pages, ensure_ascii=False) + '\n')
checks = {
    'edition': '2026-10-24',
    'chapters': sum(not page['slug'].startswith('_') for page in pages),
    'navigation_files': sum(page['slug'].startswith('_') for page in pages),
    'words_in_chapters': sum(len(page['content'].split()) for page in pages if not page['slug'].startswith('_')),
    'public_source_entries': len(public_ids),
    'background_documents': len(document_ids),
    'internal_targets_checked': len(slugs - {'_Sidebar', '_Footer'}),
    'sha256_by_page': {page['slug']: hashlib.sha256(page['content'].encode()).hexdigest() for page in pages},
}
(root / 'checks.json').write_text(json.dumps(checks, indent=2) + '\n')
print(f"Checked {checks['chapters']} chapters and {checks['navigation_files']} navigation files.")
