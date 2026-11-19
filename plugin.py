from __future__ import annotations

from LSP.plugin import LspPlugin
from LSP.plugin import OnPreStartContext
from lsp_utils import NodeManager
from pathlib import Path
import os
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
        # The server is a git pin whose engine is a git pin too. npm 12 refuses
        # that transitive git dependency, and a project .npmrc does not reach
        # the child npm that prepares it, so lsp_utils' npm gets it from the env.
        os.environ.setdefault('npm_config_allow_git', 'all')
        NodeManager.on_pre_start_async(
            context,
            cls.plugin_storage_path,
            ResourcePath('Packages', package_name, 'language-server'),
            Path('node_modules', '@markup-carve', 'carve-lsp', 'dist', 'server.js'),
            node_version_requirement='>=20',
        )
