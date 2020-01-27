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

print(points)

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

def get_closest_pt(pnt, points):
    shortest_distance = sys.maxsize
    closest_point = None
    for point in points:
        distance = get_distance(pnt, point)

        if distance < shortest_distance:
            shortest_distance = distance
            closest_point = point
        elif distance == shortest_distance:
            closest_point = None

    return str(closest_point)

count = 0

#this function checks whether the sum of all manhattan distances
#from a given point to a list of points is less than a given number 
def correct_distance(pnt, points):
    total_sum = 0
    for point in points:
        total_sum += get_distance(pnt,point)
    # print("point: {}, sum: {}".format(pnt, total_sum))
    if total_sum < 10000:
        return True
    return False

# print(correct_distance([3,2],points))  #Should be False
# print(correct_distance([4,3], points))  #should be True

#iterate through each point, incrementing count by 1
#if the sum of all its manhattan distances is less than a given number
for x in range(left, right + 1):
    for y in range(top, bottom + 1):
        if correct_distance([x,y],points):
            count += 1

print(count)




