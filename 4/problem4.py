import pprint
import re

filename = 'input.txt'

with open(filename) as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

print(type(lines[0]))

events = {}

for line in lines:
    stamp = line[1:17]
    event = line[19:] 

    if "wakes" in event:
        event = "wakes"
    elif "asleep" in event:
        event = "sleeps"
    elif re.findall(r'\d+', event) != None:
        event = int(re.findall(r'\d+', event)[0])

    # print(event)

    if stamp not in events:
        events[stamp] = event

pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(events)

guard_dict = {}

guard = None
sleep_start = None

for key in sorted(events.keys()):
    # print("timestamp: {}".format(key))
    event = events[key]

    #if a new guard started, the event will be the number of the guard
    if type(event) == int:
        guard = event
        if event not in guard_dict:
            # print("event: {}".format(event))
            guard_dict[event] = []        
    elif event == "sleeps":
        sleep_start = int(key[-2:])
    elif event == "wakes":
        # print("guard is: {}".format(guard))
        wake__time = int(key[-2:])
        for minute in range(sleep_start, wake__time):
            # print(minute)
            guard_dict[guard].append(minute)
        sleep_start = None

# pp.pprint(guard_dict)

max_min = 0
slept_most = None

#calculate which guard slept the most
for guard, minutes in guard_dict.items():
    if len(minutes) > max_min:
        max_min = len(minutes)
        slept_most = guard

#only pay attention to the minutes of the guard who slept the most
minutes_to_calculate = guard_dict[slept_most]

#keep track of how many times the guard was asleep at that particular minute
minute_counts = {}

for num in minutes_to_calculate:
    if num not in minute_counts:
        minute_counts[num] = 1
    else:
        minute_counts[num] += 1

# print(minute_counts.values())

#find during what particular minute was the guard asleep the most
max_num_min = 0
minute_slept_most = None
for key in minute_counts.keys():
    if minute_counts[key] > max_num_min:
        max_num_min = minute_counts[key]
        minute_slept_most = key

ans = minute_slept_most * slept_most

print("ans: {}".format(ans))

