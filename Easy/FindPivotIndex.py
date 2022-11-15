class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        rightSum = sum(nums)
        for i in range(len(nums)):
            rightSum -= nums[i]
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        return -1

        # variables for the left and rightmost edges of the array
        sum_left = nums[0]
        sum_right = nums[-1]

        for i in range(len(nums)):
            if nums == 1:
                sum_left[i] += sum_left[i - 1]
            if nums == sum_right:
                sum_right[i] += sum_right[i + 1]
            if nums == 0:
                sum_left[i] == sum_right[i]
            else:
                return -1
