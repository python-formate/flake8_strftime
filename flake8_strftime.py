import ast
import re
import sys
from typing import Any
from typing import Dict
from typing import Generator
from typing import List
from typing import Tuple
from typing import Type

if sys.version_info < (3, 8):  # pragma: no cover (<PY38)
    import importlib_metadata
else:  # pragma: no cover (PY38+)
    import importlib.metadata as importlib_metadata

STRFTIME001 = 'STRFTIME001 Linux-specific strftime code used.'  # noqa: E501
STRFTIME002 = 'STRFTIME002 Windows-specific strftime code used.'  # noqa: E501


class Visitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.errors: List[Tuple[int, int, str]] = []
        self._from_imports: Dict[str, str] = {}

    def visit_Str(self, node):
        for match in re.finditer(r"%-[dmHIMSj]", node.s):
            self.errors.append((
                    node.lineno,
                    node.col_offset + match.span()[0],
                    STRFTIME001,
                    ))

        for match in re.finditer(r"%#[dmHIMSj]", node.s):
            print(match)
            self.errors.append((
                    node.lineno,
                    node.col_offset + match.span()[0],
                    STRFTIME002,
                    ))


class Plugin:
    name = __name__
    version = importlib_metadata.version(__name__)

    def __init__(self, tree: ast.AST):
        self._tree = tree

    def run(self) -> Generator[Tuple[int, int, str, Type[Any]], None, None]:
        visitor = Visitor()
        visitor.visit(self._tree)

        for line, col, msg in visitor.errors:
            yield line, col, msg, type(self)
