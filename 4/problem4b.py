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

#this stores each guard as key with the value being a list of each
#minute slept
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

#guard number is key, max_num_min and minute_slept_most are stored as list of values
#max_num_min means that this is the max times a particular minute was repeated (where the guard fell asleep)
#minute_slept_most means that this is the minute where the guard fell asleep the most
final_dict = {}

for guard in guard_dict.keys():
    minutes_to_calculate = guard_dict[guard]

    minute_counts = {}
    for num in minutes_to_calculate:
        if num not in minute_counts:
            minute_counts[num] = 1
        else:
            minute_counts[num] += 1

    #find during what particular minute was the guard asleep the most
    max_num_min = 0
    minute_slept_most = None
    for key in minute_counts.keys():
        if minute_counts[key] > max_num_min:
            max_num_min = minute_counts[key]
            minute_slept_most = key

    final_dict[guard] = [max_num_min, minute_slept_most]


guard_to_return = None
minute_slept_most = None
max_num_min = 0

for guard, minute_info in final_dict.items():
    if minute_info[0] > max_num_min:
        max_num_min = minute_info[0]
        guard_to_return = guard
        minute_slept_most = minute_info[1]

answer = guard_to_return * minute_slept_most

print(answer)
