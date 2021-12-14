import collections
import re

def main(file):
    with open(file, 'r') as f:
        lines = f.readlines()

    index = 0
    line = lines[index]
    while line.strip():
        template = line.strip()
        index += 1
        line = lines[index]

    insertion_rules = {}
    for line in lines[index+1:]:
        pair, element = line.strip().split(' -> ')
        insertion_rules[pair] = element

    last = template[len(template)-1]
    pieces = [template[i:i + 2] for i in range(0, len(template) - 1)]
    parts = collections.Counter(pieces)
    print(parts)
    for step in range(1,41):
        new_parts = {}
        for part in parts.keys():
            polymer = insert_elements(insertion_rules, part)
            pieces = [polymer[i:i + 2] for i in range(0, len(polymer) - 1)]
            if step == 1:
                print(pieces)
            for piece in pieces:
                if piece in new_parts:
                    new_parts[piece] += parts[part]
                else:
                    new_parts[piece] = parts[part]
        parts = new_parts
        print(step, len(parts))

    final = {}
    for part in parts:
        print(part, parts[part])
        final[part[0]] = final[part[0]] + parts[part] if part[0] in final else parts[part]
    final[last] += 1

    print(final)
    print(max(final.values()) , min(final.values()))
    print(max(final.values()) - min(final.values()))


def insert_elements(insertion_rules, template):
    return ''.join([template[i] + insertion_rules[template[i:i + 2]] for i in range(0, len(template) - 1)]) + template[
        len(template) - 1]




def find_repeated_sequences(polymer):
    size = int(len(polymer)/2)

    while size > 5:
        count = 1
        position = size-1
        while polymer.find(polymer[0:size], position+1) != -1:
            count += 1
            position = position + size

        print(count, size)
        size -= 1

    return []




if __name__ == '__main__':
    main('input.txt')
