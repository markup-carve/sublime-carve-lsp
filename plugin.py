from __future__ import annotations

from LSP.plugin import LspPlugin
from LSP.plugin import OnPreStartContext
from lsp_utils import NodeManager
from pathlib import Path
from sublime_lib import ResourcePath
from typing import final
from typing_extensions import override


def plugin_loaded() -> None:
    LspCarvePlugin.register()


def plugin_unloaded() -> None:
    LspCarvePlugin.unregister()


@final
class LspCarvePlugin(LspPlugin):
    """Runs carve-lsp, the language server for the Carve markup language.

    The server is an npm package; lsp_utils installs it into this plugin's
    storage directory and supplies a Node runtime, so users do not need Node
    on PATH.
    """

    @classmethod
    @override
    def on_pre_start_async(cls, context: OnPreStartContext) -> None:
        package_name = cls.plugin_storage_path.name
        NodeManager.on_pre_start_async(
            context,
            cls.plugin_storage_path,
            ResourcePath('Packages', package_name, 'language-server'),
            Path('node_modules', '@markup-carve', 'carve-lsp', 'dist', 'server.js'),
            node_version_requirement='>=18',
        )
