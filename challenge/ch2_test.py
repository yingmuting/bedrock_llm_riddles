import unittest
from challenge.ch2 import *

'''
Usage: python -m unittest challenge.ch2_test
'''

class TestCh2(unittest.TestCase):
  def test_challenge2_problem0(self):
    # has number in input
    for n in range(10):
      self.assertFalse(challenge2['problems'][0]['validator']('', str(n)))
    # not enough number in response
    self.assertFalse(challenge2['problems'][0]['validator']('0', ''))
    # correct
    self.assertTrue(challenge2['problems'][0]['validator']('0123456789', ''))
    # correct with more numbers
    self.assertTrue(challenge2['problems'][0]['validator']('0123456789' * 2, ''))


  def test_challenge2_problem1(self):
    # has 3.14/6.28 in input
    self.assertFalse(challenge2['problems'][1]['validator']('', '3.14'))
    self.assertFalse(challenge2['problems'][1]['validator']('', '6.28'))
    # no 6.28 in response
    self.assertFalse(challenge2['problems'][1]['validator']('3.14', ''))
    # correct
    self.assertTrue(challenge2['problems'][1]['validator']('6.28', ''))
    # correct with more chars
    self.assertTrue(challenge2['problems'][1]['validator']('6.28' * 2, ''))
  
  def test_challenge2_problem2(self):
    # has number in input
    for n in range(10):
      self.assertFalse(challenge2['problems'][0]['validator']('', str(n)))
    # no 10000000000 in response
    self.assertFalse(challenge2['problems'][2]['validator']('0', ''))
    # correct
    self.assertTrue(challenge2['problems'][2]['validator']('10000000000', ''))
    # correct with more numbers
    self.assertTrue(challenge2['problems'][2]['validator']('10000000000' * 2, ''))