class Solution(object):
    
    def longestCommonSubsequence(self, text1, text2):
        memo = [[None for i in range(len(text1))] for j in range(len(text2))]
        
        return self.longestCommonSubsequenceHelper(text1, text2, len(text1), len(text2), memo)
    
    def longestCommonSubsequenceHelper(self, text1, text2, len1, len2, memo):
        result = 0
        if (len1 == 0 or len2 == 0):
            result = 0
        elif memo[len2-1][len1-1]:
            return memo[len2-1][len1-1]
        
        elif (text1[len1 - 1] == text2[len2 - 1]):
            result = 1+self.longestCommonSubsequenceHelper(text1, text2, len1-1, len2-1, memo)
        else:
            result = max(self.longestCommonSubsequenceHelper(text1, text2, len1, len2-1, memo), self.longestCommonSubsequenceHelper(text1, text2, len1-1, len2, memo))
        memo[len2-1][len1-1] = result
        return result

class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        return self.findTargetSumWaysHelper(0, nums, target)
     
    def findTargetSumWaysHelper(self, n, nums, target):

        if (n == len(nums)):
            return target == 0
        
        return self.findTargetSumWaysHelper(n + 1, nums, target + nums[n]) + self.findTargetSumWaysHelper(n + 1, nums, target - nums[n])
        
from collections import Counter

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        counts = Counter()
        counts[-nums[0]] += 1
        counts[nums[0]] += 1
        for num in nums[1:]:
            new = Counter()
            for key in counts.keys():
                new[key + num] += counts[key]
                new[key - num] += counts[key]
            counts = new
            print(counts)
        return counts[S]

class Solution:
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """
    def longestPalindromeSubseq(self, s):
        if len(s) < 2:
            return len(s)
            
        memo = {}
            
        maxLen = self.helper(s, 0, len(s) - 1, memo)
        
        return maxLen
        
    def helper(self, s, start, end, memo):
        if (start, end) in memo:
            return memo[(start, end)]
        if start == end:
            return 1 
        if start > end:
            return 0 
        left, right = start, end
        while left < right and s[left] != s[right]:
            right -= 1 
        if left == right:
            localMax = self.helper(s, right+1, end, memo)
        elif left + 1 == right:
            localMax = max(2, self.helper(s, right+1, end, memo))
        else:
            localMax = max(self.helper(s, left+1, right-1, memo) + 2, self.helper(s, left+1, end, memo))
            
        memo[(start,end)] = localMax
        return localMax