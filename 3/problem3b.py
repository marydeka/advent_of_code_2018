from PIL import Image, ImageDraw
img = Image.new('RGB', (1000,1000), color='white')


filename = 'input.txt'

with open(filename) as f:
    lines = f.readlines()

c = []

for line in lines:
    left, right = line.split(': ')
    id, inches = left.split('@ ')
    x1, y1 = inches.split(',')
    x1 = int(x1)
    y1 = int(y1)
    x_len, y_len = right.split('x')
    x2 = int(x_len) + x1
    y2 = int(y_len) + y1

    c.append([x1, y1, x2, y2])
    

print(c)

def overlap(x1,y1,x2, y2, x3, y3, x4, y4):
    #check if top left coordinate overlaps
    if x3 >= x1 and x3 < x2 and y3 >= y1 and y3 < y2:
        return True
    #check if bottom right coordinate overlaps
    elif x4 > x1 and x4 <= x2 and y4 > y1 and y4 <= y2:
        return True
    #check if bottom left coordinate overlaps
    elif x3 >= x1 and x3 < x2 and y4 > y1 and y4 <= y2:
        return True
    #check if top right coordinate overlaps
    elif x4 > x1 and x4 <= x2 and y3 >= y1 and y3 < y2:
        return True
    elif x3 >= x1 and x4 <= x2 and y3 <= y1 and y4 >= y2:
        return True
    

    else:
        return False
    


# print(overlap(2,1, 5,3 ,2 ,2, 8,8))
not_the_answer = set([])

all_sets = list(range(len(c)))
for i in range(len(c)):
    for j in range(len(c)):
        if i == j:
            continue
            
        overlaps = overlap(c[i][0], c[i][1], c[i][2], c[i][3], c[j][0], c[j][1], c[j][2], c[j][3])
        print(overlaps)
        if overlaps:
            not_the_answer.add(i)
            not_the_answer.add(j)
            if i in all_sets:
                all_sets.remove(i)
            if j in all_sets:
                all_sets.remove(j)

print(not_the_answer)
print(all_sets)
        # if not overlap(c[i][0], c[i][1], c[i][2], c[i][3], c[j][0], c[j][1], c[j][2], c[j][3]):
        #     print("ID is: {}".format(i))


idraw = ImageDraw.Draw(img)

for idx, rect in enumerate(c):
    if idx in all_sets:
        idraw.rectangle((rect[0], rect[1], rect[2], rect[3]), outline='red')
    else:
        idraw.rectangle((rect[0], rect[1], rect[2], rect[3]), outline='blue')

img.save('rectangle.png')










    #if you come to a square that's already been visited
    #then this ID must overlap and we want to ignore it
    # for i in range(x, x + x_len):
    #     for j in range(y, y + y_len):
    #         if matrix[i][j] == 1:
    #             break
    #         else:
    #             continue
    #         print(id)
    #         break

    #mark each visited square by incrementing value by 1
    # for i in range(x, x + x_len):
    #     for j in range(y, y + y_len):
    #         matrix[i][j] += 1

    # print(id)







