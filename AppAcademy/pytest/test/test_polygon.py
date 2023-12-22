from polygon import RegularPolygon

def test_perimeter_calculation():
    sides = 5
    length = 10
    polygon = RegularPolygon(sides, length)
    result = sides * length

    assert polygon.get_perimeter() == result