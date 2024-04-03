#!/usr/bin/env python3
#
#  __init__.py
"""
A Flake8 plugin which checks for use of platform specific strftime codes.

.. autosummary-widths:: 1/3 2/3
"""
#
#  Copyright (c) 2020-2021 Dominic Davis-Foster <dominic@davis-foster.co.uk>
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

# stdlib
import ast
import re
import sys
from typing import Dict, Union

# 3rd party
import flake8_helper

__all__ = ("Visitor", "Plugin", "SFT001", "SFT002")

__author__ = "Dominic Davis-Foster"
__copyright__ = "2020-2021 Dominic Davis-Foster"
__license__ = "MIT"
__version__ = "0.3.1"
__email__ = "dominic@davis-foster.co.uk"

SFT001 = "SFT001 Linux-specific strftime code used."
SFT002 = "SFT002 Windows-specific strftime code used."

if sys.version_info >= (3, 12):  # pragma: no cover (<py312)
	StrOrConstant = ast.Constant
else:  # pragma: no cover (py312+)
	StrOrConstant = Union[ast.Str, ast.Constant]


class Visitor(flake8_helper.Visitor):
	"""
	AST node visitor for identifying platform specific strftime codes.
	"""

	_linux_re = re.compile(r"%-[dmHIMSj]")
	_win_re = re.compile(r"%#[dmHIMSj]")

	def __init__(self) -> None:
		super().__init__()
		self._from_imports: Dict[str, str] = {}

	if sys.version_info < (3, 8):  # pragma: no cover (PY38+)

		def visit_Str(self, node: ast.Str) -> None:
			"""
			Visit an AST Str node.

			:param node: The node being visited
			"""

			self._check_linux(node)
			self._check_windows(node)

	else:  # pragma: no cover (<PY38)

		def visit_Constant(self, node: ast.Constant) -> None:
			"""
			Visit an AST Constant node.

			:param node: The node being visited
			"""

			if sys.version_info < (3, 8):  # pragma: no cover (PY38+)
				if not isinstance(node.s, str):
					return
			else:  # pragma: no cover (<PY38)
				if not isinstance(node.value, str):
					return

			self._check_linux(node)
			self._check_windows(node)

	def _check_linux(self, node: StrOrConstant) -> None:
		"""
		Perform the check for Linux-specific codes.

		:param node: The node being visited
		"""

		if sys.version_info < (3, 8):  # pragma: no cover (PY38+)
			node_value = node.s
		else:  # pragma: no cover (<PY38)
			node_value = node.value

		for match in self._linux_re.finditer(node_value):  # pylint: disable=use-list-copy
			self.errors.append((
					node.lineno,
					node.col_offset + match.span()[0],
					SFT001,  # pylint: disable=loop-global-usage
					))

	def _check_windows(self, node: StrOrConstant) -> None:
		"""
		Perform the check for Windows-specific codes.

		:param node: The node being visited
		"""

		if sys.version_info < (3, 8):  # pragma: no cover (PY38+)
			node_value = node.s
		else:  # pragma: no cover (<PY38)
			node_value = node.value

		for match in self._win_re.finditer(node_value):  # pylint: disable=use-list-copy
			self.errors.append((
					node.lineno,
					node.col_offset + match.span()[0],
					SFT002,  # pylint: disable=loop-global-usage
					))


class Plugin(flake8_helper.Plugin[Visitor]):
	"""
	A Flake8 plugin which checks for use of platform specific strftime codes.

	:param tree: The abstract syntax tree (AST) to check.
	"""

	name: str = __name__
	version: str = __version__  #: The plugin version
	visitor_class = Visitor
