class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        non_val_count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[non_val_count] = nums[i]
                non_val_count += 1

        return non_val_count