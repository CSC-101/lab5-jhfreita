import data

# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.


# Part 2
   # The function for Part 2 should be within the class in data.py.


# Part 3
# The following function takes two inputs of class Time and adds the durations of the times
# together, obeying the rules that minutes and seconds must be in the range of 0 to 60.
# The function returns the sum of the times of class Time as the output.
def add_time(Time1: data.Time, Time2: data.Time):
    Sum_hour = Time1.hour + Time2.hour
    Sum_minute = Time1.minute + Time2.minute
    Sum_second = Time1.second + Time2.second
    if Sum_second >= 60:
        Sum_second = Sum_second - 60
        Sum_minute = Sum_minute + 1
    if Sum_minute >= 60:
        Sum_minute = Sum_minute - 60
        Sum_hour = Sum_hour + 1

    return data.Time(Sum_hour, Sum_minute, Sum_second)

# Part 4
# The following function takes a list of numbers as the input and returns either "True" as
# the output if the numbers in the list are ordered in ascending order or "False" if at least
# one number is less than the previous one in the list.
def is_ascending(number_list: list):
    for i in range(1, len(number_list)):
        if number_list[i-1] > number_list[i]:
            return False
        else: continue
    return True

# Part 5
# The following function takes a list of numbers and two integers as the inputs and first
# checks that they are acceptable to perform the function on. If they are not, the function returns
# None as the output. If they are, the function outputs the index that has the largest value
# between two specified indexes represented by the two input integers.
def largest_between(number_list: list, idx1: int, idx2: int):
    if idx1 > idx2 or idx1 > len(number_list) - 1 or idx2 > len(number_list) - 1 or idx1 < 0 or idx2 < 0:
        return None
    largest_idx = idx1
    largest_value = number_list[idx1]
    for i in range(idx1, idx2):
        if number_list[i] > largest_value:
            largest_idx = i
            largest_value = number_list[i]
    return largest_idx


# Part 6
# The following function takes a list of points of class Point as the input and returns
# the index value corresponding to the point that is furthest from the origin.
def furthest_from_origin(point_list: list):
    if point_list == []:
        return None
    distance_list_squared = [p.x**2 + p.y**2 for p in point_list ]
    max_idx = 0
    max_distance = 0
    for i in range(len(point_list)):
        if distance_list_squared[i] > max_distance:
            max_distance = distance_list_squared[i]
            max_idx = i
    return max_idx
