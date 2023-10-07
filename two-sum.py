from typing import List

class Solution:
    # implementation using hashmap
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, n in enumerate(nums):
          val = target - n
          if val in hashmap:
            return [hashmap[val], i]
          hashmap[n] = i

result = Solution()
print(result.twoSum(nums = [2,7,11,15], target = 9))
