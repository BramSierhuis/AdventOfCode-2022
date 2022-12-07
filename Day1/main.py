with open("input.txt") as file_in:
    index = 0
    elves = [0]

    for line in file_in:
        if line == "\n":
            index += 1
            elves.append(0)
        else:
            elves[index] += int(line)

elves.sort(reverse=True)

total = 0
for elve in elves[:3]:
    total += elve

print(total)
