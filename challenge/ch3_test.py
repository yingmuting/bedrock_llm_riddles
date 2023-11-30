import unittest
from challenge.ch3 import *

'''
Usage: python -m unittest challenge.ch3_test
'''

class TestCh3(unittest.TestCase):
  def test_challenge3_problem0(self):
    # has 错 in input
    self.assertFalse(challenge3['problems'][0]['validator']('', '错'))
    # no 错 in response
    self.assertFalse(challenge3['problems'][0]['validator']('', ''))
    # not only 错 in response
    self.assertFalse(challenge3['problems'][0]['validator']('错错', ''))
    # correct
    self.assertTrue(challenge3['problems'][0]['validator']('错', ''))

  def test_challenge3_problem1(self):
    # has 不知道 in input
    self.assertFalse(challenge3['problems'][1]['validator']('', '不知道'))
    # no 不知道 in response
    self.assertFalse(challenge3['problems'][1]['validator']('', ''))
    # not only 不知道 in response
    self.assertFalse(challenge3['problems'][1]['validator']('不知道不知道', ''))
    # correct
    self.assertTrue(challenge3['problems'][1]['validator']('不知道', ''))

  def test_challenge3_problem2(self):
    # has 对 in input
    self.assertFalse(challenge3['problems'][2]['validator']('', '对'))
    # no 太对了 in response
    self.assertFalse(challenge3['problems'][2]['validator']('', ''))
    # not only 太对了 in response
    self.assertFalse(challenge3['problems'][2]['validator']('太对了太对了', ''))
    # correct
    self.assertTrue(challenge3['problems'][2]['validator']('太对了', ''))
