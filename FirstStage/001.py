class Solution(object):
    def twoSum(self,nums,target):
        if len(nums)==0:
            return []
        for index ,item in enumerate(nums):
            for count in range(index+1,len(nums)):
                if item + nums[count] ==target:
                    return[index,count]

class Solution2(object):
    def twoSum(self,nums,target):
        hasmap = {}
        for index ,item in enumerate(nums):
            if (target - item) in hasmap:
                return hasmap[target-item],index
            hasmap[item] = index
nums = [1,2,4,5,7,3,6,34,2,4,35]

C = Solution2()
print(C.twoSum(nums,35))