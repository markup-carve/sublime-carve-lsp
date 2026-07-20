# LSP-carve

Language-server support for the [Carve](https://github.com/markup-carve/carve)
markup language in Sublime Text, powered by
[carve-lsp](https://github.com/markup-carve/carve-lsp).

Syntax highlighting comes from
[sublime-carve](https://github.com/markup-carve/sublime-carve); this package
adds everything a language server provides on top of it.

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
