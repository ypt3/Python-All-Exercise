class RegularPolygon:
    def __init__(self, sides, length) -> None:
        self.sides = sides
        self.length = length

    def get_perimeter(self):
        return self.sides * self.length
        