# Changelog

## Unreleased

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
