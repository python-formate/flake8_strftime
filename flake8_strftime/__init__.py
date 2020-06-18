#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  __init__.py
"""
A flake8 plugin which checks for use of platform specific strftime codes using .
"""
#
#  Copyright (c) 2020 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  Based on flake8_2020
#  Copyright (c) 2019 Anthony Sottile
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.
#

__author__ = "Dominic Davis-Foster"
__copyright__ = "2020 Dominic Davis-Foster"

__license__ = "MIT"
__version__ = "0.0.0"
__email__ = "dominic@davis-foster.co.uk"



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
