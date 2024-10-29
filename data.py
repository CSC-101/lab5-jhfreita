import math
from typing import Any


# Representation of time as hours, minutes, and seconds
class Time:
    # Initialize a new Point object.
    # input: hour as an int
    # input: minute as an int
    # input: second as an int
    def __init__(self, hour: int, minute: int, second: int):
        self.hour = hour
        self.minute = minute
        self.second = second


    # Provide a developer-friendly string representation of the object.
    # input: Time for which a string representation is desired. 
    # output: string representation


    # Compare the Time object with another value to determine equality.
    # input: Time against which to compare
    # input: Another value to compare to the Time
    # output: boolean indicating equality

    # The following function takes another time object as the input and returns True if the time
    # object is equal to the given time object and false if the object is not equal to
    # the given time object.
    def __eq__(self, other):
        return type(other) == Time and self.hour == other.hour and self.minute == other.minute and self.second == other.second

# The following function takes the current time object being created as the input and
# returns a string representation of the time in terms of hours, minutes, and seconds as the output.
    def __repr__(self):
        return ("hours: {}, minutes: {}, seconds: {}".format(self.hour, self.minute, self.second))

def test_eq_Time1(self, other):
   Time1 = Time(4, 12, 42)
   Time2 = Time(4, 12, 42)
   self.assertEqual(Time1.hour, Time2.hour)
   self.assertEqual(Time1.minute, Time2.minute)
   self.assertEqual(Time1.second, Time2.second)

def test_eq_Time2(self):
    time = data.Time(2, 44, 16)
    self.assertEqual(2, time.hour)
    self.assertEqual(44, time.minute)
    self.assertEqual(16, time.second)


# Representation of a two-dimensional point.
class Point:
    # Initialize a new Point object.
    # input: x-coordinate as a float
    # input: y-coordinate as a float
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


    # Provide a developer-friendly string representation of the object.
    # input: Point for which a string representation is desired. 
    # output: string representation
    def __repr__(self) -> str:
        return 'Point({}, {})'.format(self.x, self.y)


    # Compare the Point object with another value to determine equality.
    # input: Point against which to compare
    # input: Another value to compare to the Point
    # output: boolean indicating equality
    def __eq__(self, other:Any) -> bool:
        return (other is self or
                type(other) == Point and
                math.isclose(self.x, other.x) and
                math.isclose(self.y, other.y))
