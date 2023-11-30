import unittest
from challenge.ch1 import *

'''
Usage: python -m unittest challenge.ch1_test
'''

class TestCh1(unittest.TestCase):
  def test_is_chinese_char(self):
    self.assertTrue(is_chinese_char('中'))
    self.assertFalse(is_chinese_char('a'))
    self.assertFalse(is_chinese_char('1'))
    self.assertFalse(is_chinese_char('。'))

  def test_is_chinese_str(self):
    self.assertTrue(is_chinese_str('中文'))
    self.assertFalse(is_chinese_str('中文a'))
    self.assertFalse(is_chinese_str('中文1'))
    self.assertFalse(is_chinese_str('中文。'))

  def test_is_chinese_punctuation(self):
    self.assertTrue(is_chinese_punctuation('，'))
    self.assertTrue(is_chinese_punctuation('。'))
    self.assertTrue(is_chinese_punctuation('？'))
    self.assertTrue(is_chinese_punctuation('！'))
    self.assertTrue(is_chinese_punctuation('；'))
    self.assertTrue(is_chinese_punctuation('：'))
    self.assertTrue(is_chinese_punctuation('、'))
    self.assertTrue(is_chinese_punctuation('【'))
    self.assertTrue(is_chinese_punctuation('】'))
    self.assertTrue(is_chinese_punctuation('「'))
    self.assertTrue(is_chinese_punctuation('」'))
    self.assertTrue(is_chinese_punctuation('『'))
    self.assertTrue(is_chinese_punctuation('』'))
    self.assertTrue(is_chinese_punctuation('《'))
    self.assertTrue(is_chinese_punctuation('》'))
    self.assertTrue(is_chinese_punctuation('“'))
    self.assertTrue(is_chinese_punctuation('”'))
    self.assertTrue(is_chinese_punctuation('‘'))
    self.assertTrue(is_chinese_punctuation('’'))
    self.assertTrue(is_chinese_punctuation('（'))
    self.assertTrue(is_chinese_punctuation('）'))
    self.assertTrue(is_chinese_punctuation('…'))
    self.assertTrue(is_chinese_punctuation('—'))
    self.assertFalse(is_chinese_punctuation('a'))
    self.assertFalse(is_chinese_punctuation('1'))

  def test_has_chinese_punctuation(self):
    self.assertTrue(has_chinese_punctuation('，'))
    self.assertTrue(has_chinese_punctuation('中文。'))
    self.assertFalse(has_chinese_punctuation('中文'))

  def test_remove_chinese_punctuation(self):
    self.assertEqual(remove_chinese_punctuation('，'), '')
    self.assertEqual(remove_chinese_punctuation('中文。'), '中文')
    self.assertEqual(remove_chinese_punctuation('中文'), '中文')

  def test_challenge1_problem0(self):
    # has non-chinese
    self.assertFalse(challenge1['problems'][0]['validator']('a', ''))
    # has punctuation
    self.assertFalse(challenge1['problems'][0]['validator']('中文。', ''))
    # not enough characters
    self.assertFalse(challenge1['problems'][0]['validator']('中文', ''))
    # correct
    self.assertTrue(challenge1['problems'][0]['validator']('中文中文中文中文中文中文', ''))

  def test_challenge1_problem1(self):
    # has non-chinese
    self.assertFalse(challenge1['problems'][1]['validator']('a', ''))
    # not enough characters
    self.assertFalse(challenge1['problems'][1]['validator']('中文', ''))
    # has chinese non-punctuation
    self.assertFalse(challenge1['problems'][1]['validator']('中文中文中文中文中文', ''))
    # correct
    self.assertTrue(challenge1['problems'][1]['validator']('，。？！；：、【】「」『』《》“”‘’（）…—', ''))

  def test_challenge1_problem2(self):
    # has non-chinese
    self.assertFalse(challenge1['problems'][2]['validator']('a', ''))
    # wrong number of characters
    self.assertFalse(challenge1['problems'][2]['validator']('中文中文中文中文', ''))
    self.assertFalse(challenge1['problems'][2]['validator']('中文中文中文中文中文中文中文中文', ''))
    # correct
    self.assertTrue(challenge1['problems'][2]['validator']('中文中文中文中文中文', ''))
    # correct with punctuation
    self.assertTrue(challenge1['problems'][2]['validator']('中文中文中文中文中文，。？！；：、【】「」『』《》“”‘’（）…—', ''))