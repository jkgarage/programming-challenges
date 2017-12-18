"""This is an implementation for Leetcode challenge #12.Integer to Roman

   Given an integer, convert it to a roman numeral.
   Input is guaranteed to be within the range from 1 to 3999.
   Rule of Roman numbers:
   https://www.math.nmsu.edu/~pmorandi/math111f01/RomanNumerals.html
"""

class Solution:
  ROMAN_NUMERAL_MAP = { 1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X', 40:'XL', 50:'L',
                       90:'XC', 100:'C', 400:'CD', 500:'D', 900:'CM', 
                       1000:'M', 0:'', 2000:'MM', 3000:'MMM' }
  
  def populateMapping(self, m):
    """
      Args:
        m: multipler, use to control whether it's the unit / tenth / hundreth
           / thousandth
    """
    for i in (2, 3, 6, 7, 8):
      if i < 5:
        roman = ''.join([ self.ROMAN_NUMERAL_MAP[1*m] for c in range(i)])
      else:
        roman = self.ROMAN_NUMERAL_MAP[5*m] + ''.join([ self.ROMAN_NUMERAL_MAP[1*m] for c in range(i-5)])
      self.ROMAN_NUMERAL_MAP[i*m] = roman


  def intToRoman(self, num):
    """
    :type num: int
    :rtype: str
    """
    unit = num % 10
    tenth = (num / 10) % 10 * 10
    hundredth = (num / 100) % 10 * 100
    thousandth = (num / 1000) % 10 * 1000
    
    for i in (1, 10, 100): self.populateMapping(i)
    return (self.ROMAN_NUMERAL_MAP[thousandth] + self.ROMAN_NUMERAL_MAP[hundredth] 
            + self.ROMAN_NUMERAL_MAP[tenth] + self.ROMAN_NUMERAL_MAP[unit])

  
obj = Solution()
print obj.intToRoman(1)