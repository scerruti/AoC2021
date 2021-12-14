from math import prod

def main(file):
    with open(file, 'r') as f:
        lines = f.readlines()

    score = 0
    part_2_score = []
    correct = {'{': '}', '[': ']', '(': ')', '<': '>'}
    score_table = {')': 3, ']': 57, '}': 1197, '>': 25137}
    score_2_table = {'(': 1, '[': 2, '{': 3, '<': 4}

    for line in lines:
        symbols = []
        score_2 = 0
        corrupt = False
        for char in line.strip():
            print(char, end='')
            if char in '{[(<':
                symbols.append(char)
            else:
                if len(symbols) > 0:
                    match = symbols.pop()
                    # print(char, match)
                    if correct[match] != char:
                        score += score_table[char]
                        corrupt = True
                        break
        print()
        if not corrupt:
            symbols.reverse()
            for match in symbols:
                score_2 = score_2 * 5 + score_2_table[match]
                print(match, score_2)
            part_2_score.append(score_2)

    print(score)
    part_2_score.sort()
    print(part_2_score)
    print(part_2_score[int(len(part_2_score)/2)])


if __name__ == '__main__':
    main('input.txt')
