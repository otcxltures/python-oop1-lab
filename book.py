#!/usr/bin/env python3
"""Top-level shim for CodeGrade/CI compatibility.

Some tests import `book` directly (e.g. `from book import Book`). The
actual implementation lives under the `lib` package; exposing `Book` here
lets the test suite run from the repository root without modifying tests.
"""

from lib.book import Book

__all__ = ["Book"]
