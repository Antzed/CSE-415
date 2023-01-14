import unittest


import a1


class TestA1Classes(unittest.TestCase):

    def test_rectangle(self):
        """Provided test for is_rectangle in starter code."""
        tri_1 = a1.Polygon(3, [3, 4, 5])
        self.assertEqual(tri_1.is_rectangle(), False)
        rect = a1.Polygon(4, angles=[90, 90, 90, 90])
        self.assertEqual(rect.is_rectangle(), True)
        diamond = a1.Polygon(4, [1, 1, 1, 1], [114, 66, 114, 66])
        self.assertEqual(diamond.is_rectangle(), False)
        rect_2 = a1.Polygon(4, [1, 1, 1, 1])
        self.assertEqual(rect_2.is_rectangle(), None)

    def test_rhombus(self):
        """Provided test for is_rhombus in starter code."""
        diamond = a1.Polygon(4, [1, 1, 1, 1], [114, 66, 114, 66])
        self.assertEqual(diamond.is_rhombus(), True)


    def test_square(self):
        """Provided test for is_square in starter code."""
        rect = a1.Polygon(4, angles=[90, 90, 90, 90])
        self.assertEqual(rect.is_square(), None)
        diamond = a1.Polygon(4, [1, 1, 1, 1], [114, 66, 114, 66])
        self.assertEqual(diamond.is_square(), False)
        additional = a1.Polygon(3, None, None)
        self.assertEqual(additional.is_square(), False)
        additional1 = a1.Polygon(4, [5,4,4,4])
        self.assertEqual(additional1.is_square(), False)
        additional2 = a1.Polygon(4)
        self.assertEqual(additional2.is_square(), None)
        additional3 = a1.Polygon(4, angles=[114, 66, 114, 66])
        self.assertEqual(additional3.is_square(), False)

    def test_regular_hexagon(self):
        """Provided test for is_regular_hexagon in starter code."""
        diamond = a1.Polygon(4, [1, 1, 1, 1], [114, 66, 114, 66])
        self.assertEqual(diamond.is_regular_hexagon(), False)
        hexagon_1 = a1.Polygon(6, [1] * 6)
        self.assertEqual(hexagon_1.is_regular_hexagon(), None)
        hexagon_2 = a1.Polygon(6, [1] * 6, [120] * 6)
        self.assertEqual(hexagon_2.is_regular_hexagon(), True)
        invalid = a1.Polygon(6, [5, 4, 4, 4, 4, 4])
        self.assertEqual(invalid.is_regular_hexagon(), False)
        invalid2 = a1.Polygon(6, angles=[119, 119, 119, 119, 119, 125])
        self.assertEqual(invalid2.is_regular_hexagon(), False)

    def test_isosceles_triangle(self):
        """Provided test for is_isosceles_triangle in starter code."""
        tri_1 = a1.Polygon(3, [3, 4, 5])
        self.assertEqual(tri_1.is_isosceles_triangle(), False)
        tri_2 = a1.Polygon(3, angles=[60, 60, 60])
        self.assertEqual(tri_2.is_isosceles_triangle(), True)
        tri_3 = a1.Polygon(3, [4, 4, 5])
        self.assertEqual(tri_3.is_isosceles_triangle(), True)
        tri_4 = a1.Polygon(3)
        self.assertEqual(tri_4.is_isosceles_triangle(), None)

    def test_equilateral_triangle(self):
        """Provided test for is_equilateral_triangle in starter code."""
        tri_2 = a1.Polygon(3, angles=[60, 60, 60])
        self.assertEqual(tri_2.is_equilateral_triangle(), True)
        tri_4 = a1.Polygon(3)
        self.assertEqual(tri_4.is_equilateral_triangle(), None)
        tri_5 = a1.Polygon(3, [6,6,6])
        self.assertEqual(tri_5.is_equilateral_triangle(), True)
        tri_6 = a1.Polygon(3, [6,6,7])
        self.assertEqual(tri_6.is_equilateral_triangle(), False)

    def test_scalene_triangle(self):
        """Provided test for is_scalene_triangle in starter code."""
        tri_1 = a1.Polygon(3, [3, 4, 5])
        self.assertEqual(tri_1.is_scalene_triangle(), True)
        tri_2 = a1.Polygon(3, angles=[60, 60, 60])
        self.assertEqual(tri_2.is_scalene_triangle(), False)
        notTri = a1.Polygon(4)
        self.assertEqual(notTri.is_scalene_triangle(), False)


if __name__ == '__main__':
    unittest.main()
