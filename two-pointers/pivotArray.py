'''
Leetcode proble: 2161. Partition Array According to Given Pivot
Complexity Analysis
Let N be the size of nums.

Time Complexity: O(N)

We perform a simultaneous forward and backwards iteration of nums, taking a total of O(N) time.

Space Complexity: O(N)

The algorithm uses an additional array ans of the same size as nums, which requires O(N) extra space. Other auxiliary variables, such as lessI and greaterI, require only O(1) space. Therefore, the overall space complexity is O(N) due to the extra array used to store the result. However, if we consider only the auxiliary space complexity, it would be O(1).
'''

class Solution:
    def pivotArray(self, nums, pivot):
        ans = [0] * len(nums)
        less_i = 0
        greater_i = len(nums) - 1

        for i, j in zip(range(len(nums)), range(len(nums) - 1, -1, -1)):
            if nums[i] < pivot:
                ans[less_i] = nums[i]
                less_i += 1
            if nums[j] > pivot:
                ans[greater_i] = nums[j]
                greater_i -= 1

        while less_i <= greater_i:
            ans[less_i] = pivot
            less_i += 1

        return ans