class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        min_size = len(nums) + 1

        index1: int = 0
        soma: int = 0
        for index2 in range(len(nums)):  
            soma += nums[index2]    
            if(soma < target):
                continue

            while(soma >= target):   
                if ( (index2 - index1 + 1) <= min_size):
                    min_size = (index2 - index1 + 1)
                soma -= nums[index1]
                index1 += 1
                

        if(min_size == len(nums)+1):
                return 0

        return min_size
            



        