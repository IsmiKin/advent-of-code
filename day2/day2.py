
from collections import Counter

from input_data import INPUT_DATA

box_ids_similar = Counter()

for box_id in INPUT_DATA:
    box_id_counter = Counter(box_id)
    # Get the more repeated letter and the number times it repeats
    most_commons = box_id_counter.most_common()

    already_counted_as_three = False
    already_counted_as_two = False

    for letter, repeated_times in most_commons:
        if repeated_times == 3 and not already_counted_as_three:
            already_counted_as_three = True
            box_ids_similar.update([repeated_times])
        elif repeated_times == 2 and not already_counted_as_two:
            already_counted_as_two = True
            box_ids_similar.update([repeated_times])
        else:
            continue


print(box_ids_similar)
print(box_ids_similar[2] * box_ids_similar[3])
# Solution: 6888
