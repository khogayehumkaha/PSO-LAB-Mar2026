def subarraySum(nums, k):
    d = {0:1}
    total = 0
    count = 0

    for n in nums:
        total += n
        if total - k in d:
            count += d[total - k]
        d[total] = d.get(total, 0) + 1

    return count


print(subarraySum([1,1,1], 2))