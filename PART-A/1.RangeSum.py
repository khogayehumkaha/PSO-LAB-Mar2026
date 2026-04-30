class NumArray:
    def __init__(self, nums):
        self.prefix = [0]
        for n in nums:
            self.prefix.append(self.prefix[-1] + n)

    def sumRange(self, left, right):
        return self.prefix[right+1] - self.prefix[left]
    


nums = [1,2,3,4]
obj = NumArray(nums)
print(obj.sumRange(1,3))