#Time Complexity: O(n)
#Space Complexity: O(1)
#Did it run on Leetcode: Yes

class Solution(object):
    def removeDuplicates(self, nums):
        j, count = 1, 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1
            if count <= 2:
                nums[j] = nums[i]
                j += 1
                
        return j