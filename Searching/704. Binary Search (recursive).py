# 遞迴
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        else:
            mid = len(nums)//2
            if nums[mid] == target:
                return True
            else:
                if nums[mid] < target:
                    return self.search(nums[mid+1:], target)
                else:
                    return self.search(nums[:mid], target)