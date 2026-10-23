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
| **Code actions** | Quick fixes for those diagnostics, *Align table*, CSV/TSV to pipe table and back, and *Export as Markdown / HTML* |
| **Document symbols** | Headings as an outline (`LSP: Document Symbols`) |
| **Hover** | Explains the construct under the cursor |
| **Go to definition** | Jumps a `</#id>` cross-reference, a `[^footnote]`, or a `[link][ref]` to what it names |
| **Find references** | Every use of a heading id, footnote, or reference definition |
| **Rename** | Renames an id or label and every reference to it |
| **Formatting** | `carve fmt` through the standard LSP format command |
| **Folding** | Sections, containers, and fenced blocks |
| **Completion** | Triggered on `:`, `#`, `^`, `[`, `@`, `{`, including include paths, regions and options |
| **Inlay hints** | Generated heading ids, colon-fence closers, and a hint after a bare list marker |
| **Includes** | Diagnostics, go-to-definition and completion on `{{ path }}` directives, with lint findings from included files shown on the directive - off until enabled, see [Includes](#includes) |

Colouring stays with the syntax definition by default. carve-lsp also offers
semantic tokens, which LSP applies only when its `semantic_highlighting`
setting is on. Inlay hints likewise need LSP's `show_inlay_hints` setting.

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

To bind the common ones, run **Preferences: LSP Key Bindings** from the command
palette (it opens the same user key-bindings file on the right, with LSP's own
bindings for reference on the left) and add:

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

Server options go under `settings`, with dotted keys. Each key you set here
overrides the same key in the project's `.carverc.json`; anything you leave out
comes from that file, then from the server default. So leave `settings` empty
unless you want to override the project.

```jsonc
{
	"settings": {
		"carve.format.alignTables": true,
		"carve.severities": { "table-width-total": "error" },
	},
}
```

| Setting | Default | Meaning |
|---|---|---|
| `carve.platforms` | `[]` | Extra platform lint profiles (`"github"`) |
| `carve.extensions` | `[]` | Enabled extensions, for example `"semantic-span"` |
| `carve.inlayHints` | `true` | `false` turns all inlay hints off; `{ "bareListMarkers": false }` turns off one |
| `carve.exportActions` | `true` | Offer the *Export as Markdown / HTML* actions |
| `carve.formatter` | `"conservative"` | `"migration"` opts into whole-document canonical formatting |
| `carve.format.alignTables` | `false` | Align table cells when formatting |
| `carve.severities` | `{}` | Per-code severity: `"error"`, `"warning"`, `"information"`, `"hint"` or `"off"` |
| `carve.includes.*` | | See [Includes](#includes) |

Put these keys in `settings`, not in `initializationOptions`: the server
replaces its `carve` options with whatever `settings` carries when LSP sends
it after startup, so a `carve` section in `initializationOptions` does not
stick.

### Includes

carve-lsp resolves `{{ path }}` includes only in a workspace the client reports
as trusted. Sublime Text has no notion of workspace trust, so includes are off
until you turn them on, either by trusting the workspace:

```jsonc
{
	"initializationOptions": { "workspaceTrusted": true },
}
```

or by enabling them outright with `"carve.includes.enabled": "on"` in
`settings`. Targets must stay inside the include root (the project folder, or
`carve.includes.includeRoot`), remote targets are never fetched, and depth and
size are bounded. The remaining `carve.includes.*` keys (`includeRoot`,
`allowAbsolute`, `allowedRemoteHosts`, `maxDepth`, `maxBytes`,
`maxResolverCalls`) are described in the settings schema and in the
[carve-lsp README](https://github.com/markup-carve/carve-lsp#include-settings).

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
