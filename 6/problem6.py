import sys
import pprint

filename = 'input.txt'

with open(filename) as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]
lines = [line.split(', ') for line in lines]

points = []

xs = []
ys = []

for line in lines:
    x = line[0]
    y = line[1]
    xs.append(int(x))
    ys.append(int(y))
    points.append([int(x),int(y)])

#calculate boundaries
top = min(ys)
bottom = max(ys)
left = min(xs)
right = max(xs)

print("top: {}".format(top))
print("bottom: {}".format(bottom))
print("left: {}".format(left))
print("right: {}".format(right))

def get_distance(pt_a, pt_b):
    distance = abs(pt_b[0] - pt_a[0]) + abs(pt_b[1] - pt_a[1])
    # print("     {}:{}:{}".format(pt_a,pt_b, distance))
    return distance

# print(get_distance([1,1],[3,2]))    #answer should be 3

pp = pprint.PrettyPrinter(depth=4)

label_counts = {}
# boundary_points = []

# for point in points:
#     # print(point)
#     if point[0] == left or point[0] == right or point[1] == top or point[1] == bottom:
#         # boundary_points.append(point)
#         continue
#     label_counts[str(point)] = 0

# print(label_counts)

def get_closest_pt(pnt, points):
    shortest_distance = sys.maxsize
    closest_point = None
    for point in points:
        distance = get_distance(pnt, point)
        # print("{}: {}".format(point, distance))
        if distance < shortest_distance:
            shortest_distance = distance
            closest_point = point
        elif distance == shortest_distance:
            closest_point = None
    # print(label_counts)

    return str(closest_point)

# print(get_closest_pt([2,6], points))

to_delete = []

def calculate_point():
    # print(left)
    # print(right + 1)
    for x in range(left, right + 1):
        for y in range(top, bottom + 1):
            # print(x,y)
            label = get_closest_pt([x,y], points)

            

            # print("{}, {}: {}".format(x, y, label))
            if label == 'None':
                continue
            else:

                if x == left or x == right or y == top or y == bottom:
                    if label not in to_delete:
                        to_delete.append(label)

                if label not in label_counts:
                    label_counts[label] = 1
                else:
                    label_counts[label] += 1

calculate_point()


print(to_delete)

for label in to_delete:
    del label_counts[label]
print(label_counts)

print(max(label_counts.values()))

