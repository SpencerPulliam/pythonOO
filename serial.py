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

    def __init__(self, start = 1):
        """ Create new SerialGenerator instance, initialized at 1. """

        self.start = self.increment = start

    def generate(self):
        """ Return incremented serial number. """

        self.increment += 1
        return self.increment - 1

    def reset(self):
        """ Reset the serial to the intial value of start. """

        self.increment = self.start


