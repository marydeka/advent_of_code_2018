filename = 'input.txt'

with open(filename) as f:
    lines = f.readlines()

ids = [line.strip() for line in lines]

doubles = 0
triples = 0

for id in ids:
    print(id)
    count_dict = {}
    for letter in id:
        if letter in count_dict:
            count_dict[letter] += 1
        else:
            count_dict[letter] = 1
    for value in count_dict.values():
        if value == 2:
            doubles += 1
            break
    for value in count_dict.values():
        if value == 3:
            triples += 1
            break
    print("     doubles: {}".format(doubles))
    print("         triples: {}".format(triples))

answer = doubles * triples

print(answer)