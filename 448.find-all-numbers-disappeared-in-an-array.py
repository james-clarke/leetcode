#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
#
# algorithms
# Easy (61.40%)
# Likes:    9492
# Dislikes: 498
# Total Accepted:    946.1K
# Total Submissions: 1.5M
# Testcase Example:  '[4,3,2,7,8,2,3,1]'
#
# Given an array nums of n integers where nums[i] is in the range [1, n],
# return an array of all the integers in the range [1, n] that do not appear in
# nums.
#
#
# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:
# Input: nums = [1,1]
# Output: [2]
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= n <= 10^5
# 1 <= nums[i] <= n
#
#
#
# Follow up: Could you do it without extra space and in O(n) runtime? You may
# assume the returned list does not count as extra space.
#
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = List[int]
        sorted = nums.sort
        for i, val in enumerate(sorted):
            if (val != sorted[i+1]-1):
                result.append

        return result
# @lc code=end
