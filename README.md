# sublime-carve-lsp

Language-server support for the [Carve](https://github.com/markup-carve/carve)
markup language in Sublime Text, powered by
[carve-lsp](https://github.com/markup-carve/carve-lsp).

Syntax highlighting comes from
[sublime-carve](https://github.com/markup-carve/sublime-carve); this package
adds everything a language server provides on top of it.

> **Names.** This repository is `sublime-carve-lsp`, but it installs as the
> package **`LSP-carve`** - Sublime's client packages are all named
> `LSP-<language>` (LSP-yaml, LSP-json, ...), which is how Package Control
> users find them. The same split already exists for the syntax package: the
> repo is `sublime-carve`, the package is `Carve`.
>
> Do not confuse this with [carve-lsp](https://github.com/markup-carve/carve-lsp),
> which is the **language server itself** (a TypeScript npm package used by
> VS Code, IntelliJ, Zed, and Neovim too). This repository is only the thin
> Sublime client that installs and launches it.

## Features

Advertised by carve-lsp and surfaced through the LSP package:

| Feature | What it gives you |
|---|---|
| **Diagnostics** | Markdown/Djot habits that silently produce wrong output - `**bold**` (Carve bold is a single `*`), `~~strike~~`, `+` bullets - plus unresolved references and other document problems |
| **Code actions** | Quick fixes for those migration diagnostics |
| **Document symbols** | Headings as an outline (`LSP: Document Symbols`) |
| **Hover** | Explains the construct under the cursor |
| **Go to definition** | Jumps a `</#id>` cross-reference, a `[^footnote]`, or a `[link][ref]` to what it names |
| **Find references** | Every use of a heading id, footnote, or reference definition |
| **Rename** | Renames an id or label and every reference to it |
| **Formatting** | `carve fmt` through the standard LSP format command |
| **Folding** | Sections, containers, and fenced blocks |
| **Completion** | Triggered on `:`, `#`, `^`, `[` |

Colouring stays with the syntax definition: carve-lsp deliberately does not
advertise semantic tokens, so the two layers never fight over the same text.

## Install

1. Install [LSP](https://packagecontrol.io/packages/LSP),
   [LSP-carve](https://packagecontrol.io/packages/LSP-carve) and
   [Carve](https://packagecontrol.io/packages/Carve) from Package Control.
2. Open a `.crv` file.

The server itself is an npm package. `lsp_utils` installs it into this
plugin's storage directory and provides a Node runtime, so **no global Node
installation is required**.

## Keybindings

**LSP ships its keybindings commented out**, so `F12` and friends do nothing
until you enable them - this is LSP's default, not a problem with this package.
Every feature is available immediately from the command palette
(`LSP: Goto Definition`, `LSP: Find References`, `LSP: Rename`, ...).

To bind the common ones, open **Preferences > Key Bindings** and add:

```json
[
	{
		"keys": ["f12"],
		"command": "lsp_symbol_definition",
		"args": {"side_by_side": false, "force_group": true, "fallback": false, "group": -1},
		"context": [
			{"key": "lsp.session_with_capability", "operand": "definitionProvider"},
			{"key": "auto_complete_visible", "operand": false}
		]
	},
	{
		"keys": ["f2"],
		"command": "lsp_symbol_rename",
		"context": [{"key": "lsp.session_with_capability", "operand": "renameProvider"}]
	}
]
```

The capability guard means each key keeps its normal behaviour in files no
server handles. `alt+enter` (code action) and `shift+f12` (find references) are
enabled by LSP out of the box.

## Configuration

Open **Preferences > Package Settings > LSP > Servers > LSP-carve**, or run
**Preferences: LSP-carve Settings** from the command palette.

carve-lsp reads no configuration of its own - what it reports is derived from
the document and the shared Carve corpus - so the settings file holds only the
standard LSP client options (`selector`, `initializationOptions`, `env`, and so
on).

## Relationship to the Carve package

| | [sublime-carve](https://github.com/markup-carve/sublime-carve) | LSP-carve |
|---|---|---|
| Syntax highlighting, embedded code languages | yes | no |
| Snippets, completions, build system | yes | no |
| Symbol outline | headings, from the syntax | headings, from the server |
| Cross-reference navigation | own command, single file | LSP go-to-definition and find-references |
| Formatting | runs the `carve` CLI directly | through the server |
| Diagnostics, hover, rename, code actions | no | yes |

The two are complementary: install both. sublime-carve works on its own; this
package needs it for the `text.carve` selector to match.

## License

MIT. See [LICENSE](LICENSE).
