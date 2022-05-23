class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for idx, item in enumerate(nums):
            complentment = target - item
            if complentment not in hashmap:
                hashmap[item] = idx
            else:
                return [hashmap[complentment], idx]
        