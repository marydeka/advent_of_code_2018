filename = 'input.txt'

with open(filename) as f:
    lines = f.readlines()

lines = [line.strip()for line in lines]
#take only the letters representing steps out of the lines
lines = [[line[5], line[36]] for line in lines]

# print(lines)

all_steps = {}
ordered_steps = []
removed_prereqs = []

#find out what all the possible steps are
for line in lines:
    if line[0] not in all_steps:
        all_steps[line[0]] = [""]
    if line[1] not in all_steps:
        all_steps[line[1]] = [""]

# print(all_steps)

#find all prerequisite steps for each step
for line in lines:
    prereq_step = line[0]
    step = line[1]
    current_prereq_steps = all_steps[step]
    if prereq_step not in current_prereq_steps:
        all_steps[step].append(prereq_step)


#define function to determine next step to take
def next_step(dictionary):
    possible_steps = []
    for key,value in dictionary.items():
        if value == [""] and key not in removed_prereqs:
            possible_steps.append(key)
    next_step = min(possible_steps)
    removed_prereqs.append(next_step)
    print(next_step)
    ordered_steps.append(next_step)
    print(ordered_steps)

    remove_prereq(next_step, dictionary)

#define a function to remove a prerequisite step once it's been taken
def remove_prereq(step, dictionary):
    for key, value in dictionary.items():
        if step in value:
            value.remove(step)


#continue calling next_step until all of the steps have been taken
#while loop stops when length of ordered_steps equals length of the list of all_steps keys

while len(all_steps) != len(ordered_steps):
    next_step(all_steps) 

# print("ordered steps: {}".format(ordered_steps))

answer = "".join(ordered_steps)
print(answer)



# sample_dict = {'B':['A'],'C':['B','A']}
# remove_prereq('A', sample_dict)
# print(sample_dict)