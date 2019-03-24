import copy

# 递归实现1
class Solution(object):

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.nums = nums
        self.length = len(nums)
        self.result = []
        self.Backtrace(0, [])
        return self.result

    def Backtrace(self, depth, temp):
        if depth >= len(self.nums):
            self.result.append(temp)
        else:
            for i in [True, False]:
                t = copy.deepcopy(temp)
                if i:
                    t.append(self.nums[depth])
                    self.Backtrace(depth + 1, t)
                else:
                    self.Backtrace(depth + 1, t)

# 递归实现2
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.nums = nums
        self.length = len(nums)
        self.result = []
        self.Backtrace(0,[])
        return self.result

    def Backtrace(self, depth, temp):
        self.result.append(temp[:])
        if depth < self.length:
            for i in range(depth, self.length):
                temp.append(copy.deepcopy(self.nums[i]))
                self.Backtrace(i+1,temp)
                temp.remove(temp[len(temp)-1])

# 非递归实现
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for i in range(0, len(nums)):
            for temp in result[:]:
                x = temp[:]
                x.append(nums[i])
                result.apperend(x[:])
        return result
