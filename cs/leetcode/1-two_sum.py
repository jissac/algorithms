"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i,num in enumerate(nums):
            for j in range(i+1,len(nums)):
                if num + nums[j] == target:
                    return [i,j]

#### 2nd soln using a hash map
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = {}
        for i in range(len(nums)):
            if target-nums[i]==0:
