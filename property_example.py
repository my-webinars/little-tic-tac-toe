class Circle:
    def __init__(self, diameter):
        self.diameter = diameter

    @property
    def radius(self):
        return self.diameter / 2

    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2

    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, diameter):
        if diameter <= 0:
            raise ValueError("Diameter must be positive")
        self._diameter = diameter

