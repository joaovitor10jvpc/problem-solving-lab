class Solution:
    def isPalindrome(self, s: str) -> bool:

        index1 : int = 0
        index2 : int = len(s) - 1
        
        while (index1 < index2):

            if not s[index1].isalnum():
                index1 += 1
                continue

            if not s[index2].isalnum():
                index2 -= 1
                continue   
            
            if (s[index2].lower() != s[index1].lower()):
                return False

            index1 += 1
            index2 -= 1
        
        return True