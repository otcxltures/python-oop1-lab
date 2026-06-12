#!/usr/bin/env python3

class Coffee:
    """Simple Coffee model.

    Attributes:
        size (str): Size must be one of 'Small', 'Medium', 'Large'.
        price (float): Price of the coffee.
    """

    VALID_SIZES = ("Small", "Medium", "Large")

    def __init__(self, size, price):
        # validate size through the property setter
        self._size = None
        self.size = size
        # price is a simple numeric attribute used and updated by `tip()`
        self.price = price

    @property
    def size(self):
        """Return the coffee size."""
        return self._size

    @size.setter
    def size(self, value):
        """Ensure size is one of the allowed options; print an error message otherwise.

        The tests expect the exact output string "size must be Small, Medium, or Large"
        when assignment with an invalid size occurs.
        """
        if value not in self.VALID_SIZES:
            print("size must be Small, Medium, or Large")
        else:
            self._size = value

    def tip(self):
        """Simulate leaving a tip: print a message and add 1 to the price."""
        # Note: test expects a curly apostrophe in the output string.
        print("This coffee is great, here’s a tip!")
        try:
            self.price = self.price + 1
        except Exception:
            # if price cannot be incremented, leave it unchanged
            pass