filename = 'input.txt'

with open(filename) as f:
    lines = f.readlines()

lines = lines[0].strip()

stack = []

for new_letter in lines:
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


print(len(stack))

