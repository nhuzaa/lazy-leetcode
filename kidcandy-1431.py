def kidWithCandies(candies: list[int], extranCandies: int) -> list[bool]:

    maxCandy = max(candies)
    output = []

    for x in candies:
        if x + extranCandies >= maxCandy:
            output.append(True)
        else:
            output.append(False)

    return output


candies = [12, 1, 12]
extraCandies = 10


output = kidWithCandies(candies, extraCandies)

print(output)
