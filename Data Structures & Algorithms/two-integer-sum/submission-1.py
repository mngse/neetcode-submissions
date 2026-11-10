class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
#        for i in range(len(nums)):
#            for j in range(i+1, len(nums)):
#                if nums[i] + nums[j] == target:
#                    return [i,j]

        compl = {}
        
        for i in range(len(nums)):
            if nums[i] in compl:
                return [compl[nums[i]], i]
            compl[target - nums[i]] = i
            

# 1) i = 0, target - num[0] = 4 in compl? no -> compl = {4:0, }
# 2) i =1, 7-4=3 in compl? no -> compl = {4:0, 3:1}