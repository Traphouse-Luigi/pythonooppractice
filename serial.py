"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, a=0):
        """Make a new generator starting at 'a'"""
        self.a = self.b = a

    def __repr__(self):
        """Show 'a' as the first value in the generator"""
        return f'<Serial Generator start = {self.b}, next = {self.a}>'

    def generate(self):
        """Increment the value by one and return the new value"""
        self.a = self.a + 1
        return self.a - 1

    def reset(self):
        """The original value is stored in a separate variable, which allows us to return to it at any given point"""
        self.a = self.b
