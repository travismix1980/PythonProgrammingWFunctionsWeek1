import unittest
import math

from datetime import datetime


# get needed tire information and convert to int
tire_width = int(input("input the width of the tire: "))
tire_ratio = int(input("input the aspect ratio of the tire minus any letters: "))
tire_diameter = int(input("input the diameter of the tire: "))

# calculate the approx volume of the tire
def calculate_tire_volume(width, ratio, diameter):
    volume = math.pi * (width ** 2) * (ratio * (width * ratio + 2540 * diameter)) / 10_000_000_000
    
    #store date time and other info to volumes.txt
    current_date_time = datetime.now()
    with open("volumes.txt", "at") as v:
        print(f"{current_date_time:%Y-%m-%d}, {width}, {ratio}, {diameter}, {volume:.2f}", file=v)
    
    return f"The approximate volume is {volume:.2f}"

def user_purchase():
    purchase = input("Would you like to buy the tires (y or n)? ")
    purchase = purchase.lower()
    if purchase == 'y':
        phone_number = input("please enter your phone number for someone to call about the purchase: ")
        with open("volumes.txt", "at") as v:
            print(f"Phone number: {phone_number}", file=v)
    
#output volume
print(f"{calculate_tire_volume(tire_width, tire_ratio, tire_diameter)}")

# ask for purchase
user_purchase()

# run test cases comment out this section to avoid running tests
# class TestTireVolume(unittest.TestCase):
#     def test_tire_one(self):
#         self.assertEqual(calculate_tire_volume(185, 50, 14), "The approximate volume is 24.09", "test failed")
        
#     def test_tire_two(self):
#         self.assertEqual(calculate_tire_volume(205, 60, 15), "The approximate volume is 39.92", "test failed")
        

# unittest.main()