import data
import lab5
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.


    # Part 3
    def test_add_time1(self):
        Time1 = data.Time(4, 28, 56)
        Time2 = data.Time(6, 44, 16)
        self.assertEqual(lab5.add_time(Time1, Time2), data.Time(11, 13, 12))

    def test_add_time2(self):
        Time1 = data.Time(3, 5, 14)
        Time2 = data.Time(1, 7, 18)
        self.assertEqual(lab5.add_time(Time1, Time2), data.Time(4, 12, 32))

    # Part 4
    def test_is_ascending1(self):
        lista = [4, 2, 4, 5, 6, 7]
        self.assertEqual(lab5.is_ascending(lista), False)

    def test_is_ascending2(self):
        listb = [1, 2, 2, 2, 3, 8]
        self.assertEqual(lab5.is_ascending(listb), True)



    # Part 5
    def test_largest_between1(self):
        lista = [1, 7, 84, -4, -8, 56, 14, 2, 2, 56, 8]
        self.assertEqual(lab5.largest_between(lista, 4, 8), 5)

    def test_largest_between2(self):
        listb = [12, 72, -16, 45, 44, 45, 45, 44, 42, 56, 8]
        self.assertEqual(lab5.largest_between(listb, 6, 2), None)

    # Part 6
    def test_furthest_from_origin1(self):
        point_list1 = [data.Point(4, 2), data.Point(8,0), data.Point(-5,3), data.Point(8,-4), data.Point(-10,2), data.Point(5,7)]
        self.assertEqual(lab5.furthest_from_origin(point_list1), 4)

    def test_furthest_from_origin2(self):
        point_list2 = []
        self.assertEqual(lab5.furthest_from_origin(point_list2), None)


if __name__ == '__main__':
    unittest.main()
