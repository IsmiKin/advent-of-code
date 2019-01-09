
from collections import Counter

from input_data import INPUT_DATA

box_ids_similar_counter = Counter()
# we will use a set because it's works as a dict in adding,
# we could also use a dictionary and check later the keys
box_ids_similar = set()


for box_id in INPUT_DATA:
    box_id_counter = Counter(box_id)
    # Get the more repeated letter and the number times it repeats
    most_commons = box_id_counter.most_common()

    already_counted_as_three = False
    already_counted_as_two = False

    for letter, repeated_times in most_commons:
        if repeated_times == 3 and not already_counted_as_three:
            already_counted_as_three = True
            box_ids_similar_counter.update([repeated_times])
        elif repeated_times == 2 and not already_counted_as_two:
            already_counted_as_two = True
            box_ids_similar_counter.update([repeated_times])
        else:
            continue

    if already_counted_as_two or already_counted_as_three:
        box_ids_similar.add(box_id)


print('Number of boxes with 2 and 3 repeated letters -> {}'.format(box_ids_similar_counter))
print('Checksum: {}'.format(box_ids_similar_counter[2] * box_ids_similar_counter[3]))
# Solution: 6888

# Part 2

# Find the boxes with full of fabric
# The boxes will have IDs which differ by exactly one character at
# the same position in both strings.
boxes_with_fabric = []
diff_letter_index = None

while(len(box_ids_similar) > 0 and len(boxes_with_fabric) <= 0):
    current_box_id = box_ids_similar.pop()
    current_box_id_counter = Counter(current_box_id)

    for checkin_box_id in box_ids_similar:
        checking_box_id_counter = Counter(checkin_box_id)
        # if they have the diff between the number of letters between to boxid
        # it means they are candidates
        letters_diff = current_box_id_counter - checking_box_id_counter
        if len(letters_diff) == 1:
            letter_diffs_number = 0

            # check letter by letter if are the same. if only one fails,
            # both are the choosen ones
            for letter_index, (letter_box_id_1, letter_box_id_2) in enumerate(zip(current_box_id, checkin_box_id)):
                if letter_box_id_1 != letter_box_id_2:
                    letter_diffs_number += 1
                    diff_letter_index = letter_index

                if letter_diffs_number > 1:
                    break

            # We found the boxes
            if letter_diffs_number == 1:
                boxes_with_fabric.append(current_box_id)
                boxes_with_fabric.append(checkin_box_id)

print('Boxes with fabric: {}'.format(boxes_with_fabric))
# remove the different letter
# TODO: pass linter
common_letters_boxs_ids = boxes_with_fabric[0][:diff_letter_index] + boxes_with_fabric[0][diff_letter_index + 1:]
print('Common letters between both box ids: {}'.format(common_letters_boxs_ids))
