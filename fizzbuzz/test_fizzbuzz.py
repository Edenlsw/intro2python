import unittest  # importing python default test library

# from fizzbuzz import generate
from fizzbuzz import challenge 

# class TestFizzBuzz(unittest.TestCase): # sets up test case
#   def test_lists_values_up_to_one(self): # the test. must include self. 
#     self.assertEqual(generate(1), "1")

#   def test_lists_values_up_to_two(self):
#     self.assertEqual(generate(2), "2")

# =================================== test passes for basic fizz buzz 
# class TestFizzBuzz(unittest.TestCase):
#   def test_display_fizz(self):
#     self.assertEqual(challenge(3), "Fizz")
  
#   def test_display_buzz(self):
#     self.assertEqual(challenge(5), "Buzz")

#   def test_display_fizzbuzz(self):
#     self.assertEqual(challenge(15), "FizzBuzz")

# -----------=====================================

class TestFizzBuzz(unittest.TestCase):
  # def test_fizz(self):
  #   self.assertEqual(challenge(3), "Fizz")
  
  # def test_display_buzz(self):
  #   self.assertEqual(challenge(5), "Buzz")

  
  def test_fizz(self):
    for i in [3, 6, 9, 18]:
      print('testing', i)
      assert challenge(i) == 'Fizz'

  def test_fizzbuzz(self):
    for i in [15, 30, 45]:
      print('testing', i)
      assert challenge(i) == "FizzBuzz"
   
  def test_buzz(self):
    for i in [5, 20, 25]:
      print('testing', i)
      assert challenge(i) == "Buzz"








