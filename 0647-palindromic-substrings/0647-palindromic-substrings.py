class Solution:
    def countSubstrings(self, s: str) -> int:
        n, ans = len(s), 0
        
        def palindromeCount(left: int, right: int) -> int:
            count = 0
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
            return count
        
        for i in range(n):
            even = palindromeCount(i, i + 1)
            odd = palindromeCount(i, i)
            ans += even + odd
            
        return ans
# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         def checkPal(stri):
#             r = len(stri) -1 
#             for l in range(len(stri)//2):
#                 if stri[l] != stri[r]: return False
#                 r-=1   
#             return True  
#         # @cache
#         def rec(i, strA):
#             print(i, strA)
#             if (strA and not checkPal(strA)) or i >= len(s): return []
#             return max(1+ rec(i+1,strA.append(s[i])),  rec(i+1,[]))

#         return rec(0,[])