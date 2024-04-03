def countSegments(s: str) -> int:
    if s == "" or s == " ":
        return 0
    list_string = s.split(" ")

    while "" in list_string:
        list_string.remove("")

    len_str = len(list_string)

    return len_str


input = "Of all the gin joints in all the towns in all the world,   "
output = countSegments(input)

print(output)
