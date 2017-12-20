"""This is an implementation for Leetcode challenge #48.Rotate Image

   You are given an n x n 2D matrix representing an image.
   Rotate the image by 90 degrees (clockwise).
   You have to rotate the image in-place, which means you have to modify the input 2D matrix directly
"""

class Solution(object):
  
  def niceprint(self, image):
    leng = len(image)
    print '['
    for i in xrange(leng):
      print ' '.join(str(x) for x in image[i])
    print ']'

    
  def rotate(self, image):
    leng = len(image)
    for i in xrange(leng/2):
      for j in xrange(i, leng-i-1):
        """
        # move layer by layer, like those of an onion
        i,j => j, len-1-i
        j, len-1-i => len-1-i, len-1-j
        len-1-i, len-1-j => len-1-j, i
        len-1-j, i => i, j
        """
        temp = image[i][j]
        image[i][j] = image[leng-1-j][i]
        image[leng-1-j][i] = image[leng-1-i][leng-1-j]
        image[leng-1-i][leng-1-j] = image[j][leng-1-i]
        image[j][leng-1-i] = temp
    return image


obj = Solution()
image = [
  [1, 2, 3, 4, 5],
  [8, 7, 8, 9, 4],
  [2, 3, 7, 7, 3],
  [5, 7, 3, 4, 9],
  [2, 7, 3, 8, 2] 
]
"""
image = [
  [ 1 ]
]
"""
obj.niceprint(image)
print '\nRotated image:'
obj.niceprint(obj.rotate(image))