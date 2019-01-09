
from input_data import INPUT_DATA

from collections import Counter

# Part 2

# Counter collection class is used because its a dict subclass
# for counting hashable objects. In other languages i would use just
# a normal dictionary

current_frequency = 0

frequency_records = Counter([current_frequency])
first_frequency_repeated_twice = None

while not first_frequency_repeated_twice:
    # Time complexity: O(n)
    for frequency in INPUT_DATA:
        current_frequency += int(frequency)
        frequency_records.update([current_frequency])
        if frequency_records[current_frequency] == 2:
            first_frequency_repeated_twice = current_frequency
            break

print(first_frequency_repeated_twice)
