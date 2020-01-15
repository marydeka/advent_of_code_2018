filename = 'input.txt'

with open(filename) as f:
    lines = f.readlines()

lines = lines[0].strip()

def react(arr):
    stack = []

    for new_letter in arr:
        # print("new_letter: {}".format(new_letter))
        if len(stack) == 0:
            stack.append(new_letter)
        elif len(stack) > 0:
            top_letter = stack[-1]
            # print("top_letter: {}".format(top_letter))
            if top_letter != new_letter and top_letter.lower() == new_letter.lower():
                stack.pop()
            else:
                stack.append(new_letter)
    return len(stack)

letters = {}
different_reactions = []

for letter in lines:
    l_letter = letter.lower()
    if letter not in letters:
        letters[l_letter] = letter

# print(letters.values())

for reaction_letter in letters.values():
    # print("reaction letter: {}".format(reaction_letter))
    current_stack = []
    for new_letter in lines:
        # print("     new_letter: {}".format(new_letter))
        if new_letter.lower() != reaction_letter.lower():
            current_stack.append(new_letter)
            # print("current stack: {}".format(current_stack))
            
    different_reactions.append(current_stack)

#keep track of the final lengths of each array after they've reacted
final_lengths = []

for str_arr in different_reactions:
    reaction_length = react(str_arr)
    final_lengths.append(reaction_length)

# print(final_lengths)
print(min(final_lengths))