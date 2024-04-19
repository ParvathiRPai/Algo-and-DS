# longest common substring
#Input: s1 = "abdca"
# s2 = "cbda"
# Output: 2
# Explanation: The longest common substring is "bd".

class Solution:
  def findLCSLength(self, s1, s2):
      return self.recursive(s1, s2, 0, 0, 0)
  
  def recursive(self, s1, s2, i1, i2, count):
      if i1==len(s1) or i2==len(s2):
          return count
      
      if s1[i1]==s2[i2]:
          count=self.recursive(s1, s2, i1+1, i2+1, count+1)
      
      c1=self.recursive(s1, s2, i1, i2+1, 0)
      c2=self.recursive(s1, s2, i1+1, i2, 0)
      
      return max(count, max(c1, c2))
      
      
class Solution:
  def findLCSLength(self, s1, s2):
      n1 = len(s1)
      n2 = len(s2)
      maxLen = min(n1, n2)
      dp = [[[-1 for i in range(maxLen)] for j in range(n2)] for k in range(n1)]
      return self.recursive(dp, s1, s2, 0, 0, 0)
  
  def recursive(self, s1, s2, i1, i2, count):
      if i1==len(s1) or i2==len(s2):
          return count
      
      if dp[i1][i2][count]==-1:
          c1= count
          if s1[i1]==s2[i2]:
              c1= self.recursive(dp, s1, s2, i1+1, i2+1, count+1)
        
        c2 = elf.recursive(dp, s1, s2, i1, i2+1, 0)
        c3 = elf.recursive(dp, s1, s2, i1+1, i2, 0)
        dp[i1][i2][count]=max(c1, max(c2, c3))
    return dp[i1][i2][count]


     
class Solution:
  def findLCSLength(self, s1, s2):
      n1 = len(s1)
      n2 = len(s2)
      maxLen = 0
      dp = [[0 for i in range(n2+1)] for j in range(n1+1)]
      
      for i in range(1, n1+1):
          for j in range(1, n2+1):
              if s1[i-1]==s2[j-1]:
                  dp[i][j]=1+dp[i-1][j-1]
                  maxLen = max(maxLen, dp[i][j])
    return maxLen
