class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0 ,len(nums) - 1
        while l <= r:
            mid = (l + r)//2
            print(l,r,mid)
            if nums[mid] == target:
                return True
            elif nums[l] == nums[r] == nums[mid]:
                l +=1
                r -=1
            elif nums[l] <= nums[mid] and nums[l] <= target < nums[mid]:
                r = mid - 1
            elif nums[mid] <= nums[r] and nums[mid] <= target <= nums[r]:
                l = mid + 1
            elif (nums[l] <= nums[mid]) == False:
                r = mid - 1
            else:
                l = mid + 1
        return False