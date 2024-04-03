def thousandSeparator(n: int) -> str:

    bunch = list()
    output = str(n)
    while n > 0:
        last_digits = n % 1000
        n = n // 1000
        bunch.insert(0, str(last_digits))

    print("bunch", bunch)

    if len(bunch) > 0:
        output = bunch[0]
        for c in bunch[1:]:
            output += f".{c}"
    return output


input = 51040
# input = 1234
#

# bunch ['51', '40']
# 51.40

output = thousandSeparator(input)

print(output)
