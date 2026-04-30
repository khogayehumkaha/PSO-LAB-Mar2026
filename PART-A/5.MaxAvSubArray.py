def findMaxAverage(nums, k):
    window = sum(nums[:k])
    max_sum = window

    for i in range(k, len(nums)):
        window += nums[i] - nums[i-k]
        max_sum = max(max_sum, window)

    return max_sum / k

print(findMaxAverage([1,12,-5,-6,50,3], 4))