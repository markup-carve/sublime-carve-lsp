# Changelog

## 0.1.6

Sublime now bundles carve-lsp 0.1.15, including the carve-js 0.1.15 engine.

### Improvements

- The bundled language server follows the latest published Carve parsing and task-state behavior (#17).

**Full Changelog**: https://github.com/markup-carve/sublime-carve-lsp/compare/0.1.5...0.1.6

## 0.1.5

- Bundle carve-lsp 0.1.14 (from 0.1.12), whose engine is carve-js 0.1.13 (#14).
  Diagnostics follow the 0.1.11 spec (continuation markers, CSV/TSV table
  fences, include regions), lint covers included files, and new quick fixes
  and table conversion actions are available.
- Document the server's `carve` settings and `carve.includes.*` in the
  settings schema and README (#14).
- Expose `initializationOptions.workspaceTrusted`, off by default, so includes
  can be turned on in Sublime Text (#14).
- Require Node 20, as the bundled engine declares (#14).

## 0.1.4

- Bundle carve-lsp 0.1.12 (from 0.1.9), whose engine is carve-js 0.1.11
  (#12, #13). Headings, folds and semantic tokens reach blocks inside list items,
  definitions and footnote bodies, footnote navigation and rename work
  against the 0.1.11 engine, and diagnostics keep their range after an emoji
  on the line. The server keeps running when the editor refuses one of its
  capability registrations, and Enter after a `:::` or code fence opener
  leaves the cursor on the new body line.

## 0.1.3

- Bundle carve-lsp 0.1.9, whose engine resolves to carve-js 0.1.10 instead of
  0.1.7. Names now compare case exactly, so a cross-reference whose case does
  not match its target is reported: `</#plan>` against a heading written
  `{#Plan}` draws a `broken-crossref` where the previous server reported
  nothing at all and the reference silently pointed at the differently-cased
  heading.

## 0.1.2

- Bundle carve-lsp 0.1.7, five releases on from the 0.1.2 this package shipped
  before 0.1.1 was cut. It brings include resolution (definition, completion and
  diagnostics on a `{{ path }}` directive, on a `@lines` range and on a named
  section), crossrefs that resolve across an include, workspace intelligence,
  pull diagnostics, colon-fence tooling and safe fixes. The engine underneath it
  moves from carve-js 0.1.3 to 0.1.7.

## 0.1.1

- Menu: only extend the LSP > Servers submenu, dropping the duplicate top-level
  entry, to match the other `LSP-*` packages.
- Expose a `server_path` setting (default `auto`) so a locally installed server
  can be used instead of the managed one; documented in the settings schema.
- Ship `language-server/package-lock.json` in the release archive for
  consistent dependency installs.
- Enable Renovate to auto-bump the bundled `@markup-carve/carve-lsp` server.
- README: recommend `Preferences: LSP Key Bindings` for adding keybindings.

## 0.1.0

- Initial package: runs [carve-lsp](https://github.com/markup-carve/carve-lsp)
  for `.crv` documents, installed through `lsp_utils` with a managed Node
  runtime. Brings diagnostics, code actions, hover, document symbols, go-to
  definition, find references, rename, formatting, folding, and completion to
  Sublime Text.
