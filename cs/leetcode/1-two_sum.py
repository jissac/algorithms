"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

https://leetcode.com/problems/two-sum/
"""
from __future__ import annotations

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

    def twoSum_hash(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hmap = {}
        for i in range(len(nums)):
            key = target - nums[i]
            if key in hmap:
                return [i, hmap[key]]
            hmap[nums[i]] = i

## REDO OF THE SOLUTION ##

# brute force (n*n) -> O(n^2)
def twoSum(nums: list[int], target: int) -> list[int] | None:
    for i,val in enumerate(nums):
        print(i,val)
        for j in range(i+1, len(nums)):
            if val + nums[j] == target:
                return[i,j]
    print("Two sum target not found")
    return None

# x+y=target, targt-x = y -> does y exist in array?
# use a hashmap to store values
# time: O(n), space: O(n)
def twoSum_hash(nums: list[int], target: int) -> list[int] | None:
    hmap = {}
    for i,num in enumerate(nums):
        y = target-num
        print(y)
        if y in hmap:
            return [i,hmap[y]]
        hmap[num] = i
        print(hmap)  

if __name__ == "__main__":
    nums =  [2,7,11,15]
    target = 9
    # print("bruteFORCE")
    # twoSum(nums,target)
    print("HashMap")
    out = twoSum_hash(nums,target)
    out.sort()
    print("Solution:",out)