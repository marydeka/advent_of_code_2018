filename = 'input.txt'

with open(filename) as f:
    lines = f.readlines()

lines = [int(line.strip()) for line in lines]

# print(lines)

frequency = 0
frequencies = {}

while frequency not in frequencies:
    for line in lines:
        frequencies[frequency] = frequency
        # print(frequency)
        # print("line: {}".format(line))
        frequency += line
        if frequency in frequencies:
            break

print("frequency: {}".format(frequency))





