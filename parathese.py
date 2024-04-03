

def isValid(s):
    stack = []
    map = {
        '(': ')',
        '{': '}',
        '[': ']',
    }

    for char in s:
        if char in map:
            stack.append(char)
        elif len(stack) == 0  or char != map[stack.pop()]:
            return False

    if len(stack) == 0:
        return True

    return False



s = "(}}}})" # input
output =  isValid(s) # o    

print("output", output)

