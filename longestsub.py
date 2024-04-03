def lengthOfLongestSubstring(s: str) -> int:
    sub_strings = list()

    new_sub_string = ""

    for c in s:
        if c in new_sub_string:
            sub_strings.append(new_sub_string)
            new_sub_string = c
        else:
            new_sub_string += c

    max = 0
    print(sub_strings)
    for sub in sub_strings:
        if max < len(sub):
            max = len(sub)

    return max


# input = "abcabcbb"
# input = "bbbbb"
input = "pwwkew"


output = lengthOfLongestSubstring(input)

print(output)
