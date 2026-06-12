#!/usr/bin/env python3

class Book:
    """Simple Book model.

    Attributes:
        title (str): The book's title.
        page_count (int): Number of pages in the book. Must be an integer.
    """

    def __init__(self, title, page_count):
        # store title directly; no validation required by the tests
        self.title = title
        # use the property setter to validate page_count
        self._page_count = None
        self.page_count = page_count

    @property
    def page_count(self):
        """Return the page count."""
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        """Ensure page_count is an integer; print an error message otherwise.

        The tests expect the exact output string "page_count must be an integer" when
        assignment with a non-int occurs.
        """
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value

    def turn_page(self):
        """Simulate turning a page by printing the expected message."""
        print("Flipping the page...wow, you read fast!")

        