# Maintaining this overview

The native GitHub Wiki is the reading destination. The `wiki/` directory keeps an editable source copy in the main repository. The two Git repositories have separate histories; a main-repository commit does not publish a Wiki edit automatically.

## Change the content

Edit the relevant Markdown source and the matching native Wiki page. Preserve its title and slug so existing links continue to work. The order and titles are recorded in `wiki/page-order.json`. `_Sidebar.md` and `_Footer.md` are GitHub's reserved navigation files.

Use dated primary sources for changing public facts. Keep personal recollections identified, distinguish proposals from accepted commitments, and record a substantive change in the current-position chapter. Preserve the intended reciprocal meaning of C-Hours. The overview's scope intentionally leaves private intimate and family matters outside the public account.

## Prepare the publishing bundle

Run from the repository root:

```sh
python tools/prepare_wiki.py
```

This reads the Markdown pages in the recorded order, checks local Wiki targets and source references, and refreshes `wiki/publish-bundle.json` and `checks.json`. It does not publish to GitHub or make network requests. The bundle contains the exact page text and is an aid for keeping the two destinations consistent.

## Publish with a Wiki checkout

GitHub's native Wiki is a separate repository:

```sh
git clone https://github.com/auraofintelligence/Paul-overview-handover.wiki.git
```

With appropriate GitHub access, copy the `.md` files from `wiki/` into that checkout, review the diff, commit and push. Keep the checkout's `.git` directory intact. JSON files belong in the main repository, not the Wiki checkout.

Alternatively, use the native Wiki's New page and Edit actions, with the exact title and content in the bundle. Publish `_Sidebar` and `_Footer` through their corresponding Wiki controls. After publishing, inspect Home, the navigation, representative chapters and source links in the native Wiki.

## Editorial boundaries

Do not turn a meeting into an endorsement, a submission into funding, a proposed facility into an operating service, a simulation into engineering validation or a research target into a demonstrated forecast. These distinctions support an accurate handover while retaining the full ambition of the work.

The current work is Luke's proposal. An incoming participant's accepted responsibilities need their own explicit record. Original material, cultural permissions and third-party rights retain their respective terms.
