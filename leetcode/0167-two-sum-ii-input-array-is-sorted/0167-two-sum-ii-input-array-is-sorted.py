class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        index1: int = 0
        index2: int = len(numbers) - 1

        while (index1 < index2):
            
            sum: int = numbers[index1] + numbers[index2]

            if (sum == target):
                return [index1 + 1, index2 + 1]

            #se a soma for maior, index2 -= 1
            if (sum > target):
                index2 -= 1

            #se a soma for menor, index1 += 1
            if (sum < target):
                index1 += 1

        return []


        

        