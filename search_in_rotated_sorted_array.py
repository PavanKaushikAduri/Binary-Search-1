#Time Complexity : O(log n)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No


# Your code here along with comments explaining your approach in three sentences only

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target: return mid
            if nums[low] <= nums[mid]:
                if nums[low] <= target and nums[mid] >= target:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target and nums[high] >= target:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
        
