filename = 'input.txt'

with open(filename) as f:
    lines = f.readlines()

ids = [line.strip() for line in lines]

first_id = None
second_id = None

for id_1 in range(len(ids)):
    for id_2 in range(id_1 + 1, len(ids)):
        differences = 0
        for index in range(len(ids[0])):
            if ids[id_1][index] != ids[id_2][index]:
                differences += 1
        if differences == 1:
            first_id = ids[id_1]
            second_id = ids[id_2]
            break

print(first_id)
print(second_id)

print("common letters are: ", end = ' ')

for index in range(len(first_id)):
    if first_id[index] == second_id[index]:
        print(first_id[index], end = '')

print('\n')

