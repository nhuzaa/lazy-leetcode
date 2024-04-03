
class Solution:
    def reverse(self, x: int) -> int:

        newNum = 1
        div =  2
        while x > 1:
            rem = x % 10
            x = x // 10
            print(div, rem)
            newNum = newNum * 10 + rem

        return  newNum




val = 123
sol = Solution() 

print('Rever' , sol.reverse(val))

print('Rever' , sol.reverse( -123))

