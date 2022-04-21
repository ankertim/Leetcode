class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = len(nums)
        flag = True
        while(flag):
            if val in nums:
                nums.remove(val)
            else:
                flag = False
        return count