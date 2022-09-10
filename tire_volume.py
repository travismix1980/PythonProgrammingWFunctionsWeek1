import unittest
import math


# get needed tire information and convert to int
tire_width = int(input("input the width of the tire: "))
tire_ratio = int(input("input the aspect ratio of the tire minus any letters: "))
tire_diameter = int(input("input the diameter of the tire: "))

# calculate the approx volume of the tire
def calculate_tire_volume(width, ratio, diameter):
    volume = math.pi * (width ** 2) * (ratio * (width * ratio + 2540 * diameter)) / 10_000_000_000
    return f"The approximate volume is {volume:.2f}"

#output volume
print(f"{calculate_tire_volume(tire_width, tire_ratio, tire_diameter)}")

#run test cases comment out this section to avoid running tests
#adjust approximate value strings to make tests fail 
class TestTireVolume(unittest.TestCase):
    def test_tire_one(self):
        self.assertEqual(calculate_tire_volume(185, 50, 14), "The approximate volume is 24.09", "test failed")
        
    def test_tire_two(self):
        self.assertEqual(calculate_tire_volume(205, 60, 15), "The approximate volume is 39.92", "test failed")
        

unittest.main()