import asyncio
from pathlib import Path
from typing import Union

from magic_tree.controller.builders.directory_tree_builder import DirectoryTreeBuilder
from magic_tree.magic_tree_dictionary import MagicTreeDictionary


async def auto_document(path: Union[Path, str]):
    document_tree = DirectoryTreeBuilder.from_path(path=document_root_path)
    print(document_tree)

if __name__ == "__main__":
    document_root_path = Path(__file__).parent.parent.parent / "document"
    asyncio.run(auto_document(document_root_path))
