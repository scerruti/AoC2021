import itertools

def main(file):
    with open(file, 'r') as f:
        lines = f.readlines()

    count = len(list(filter(lambda x: len(x) in [2,3,4,7],
    list(itertools.chain(*[line.strip().split(" | ")[1].split(" ") for line in lines])))))

    print(list(filter(lambda x: len(x) in [1,4,7,8], list(itertools.chain(*[line.strip().split(" | ")[1].split(" ") for line in lines])))))
    print(count)

    segment = [None]*7

    total = 0
    for line in lines:
        [input, output] = line.strip().split(" | ")
        input_digits = [set(digit) for digit in input.split(" ")]
        output_digits = [set(digit) for digit in output.split(" ")]

        digits = input_digits.copy()
        digits.extend(output_digits)

        two_segment = list(filter(lambda x: len(x) == 2, digits))
        segment[2] = segment[5] = letters_from(two_segment)

        five_segment = list(filter(lambda x: len(x) == 5, digits))
        five_segment = [s.difference(segment[2]) for s in five_segment]
        letters = letters_from(five_segment)
        horizontal = set().union(*list(filter(lambda s: len(s) == 3, five_segment)))

        segment[0] =  segment[3] = segment[6] = horizontal
        segment[1] = segment[4] = letters.difference(horizontal)

        three_segment = list(filter(lambda x: len(x) == 3, digits))
        three_segment = [s.difference(segment[2]) for s in three_segment]
        segment[0] = letters_from(three_segment)
        segment[3] = segment[3].difference(segment[0])
        segment[6] = segment[6].difference(segment[0])

        four_segment = list(filter(lambda x: len(x) == 4, digits))
        four_segment = letters_from(four_segment).difference(segment[2])
        segment[1] = segment[1].intersection(four_segment)
        segment[4] = segment[4].difference(segment[1])
        segment[3] = segment[3].intersection(four_segment)
        segment[6] = segment[6].difference(segment[3])

        six_segment = list(filter(lambda x: len(x) == 6, digits))
        six_segment = [s.difference(four_segment)
                        .difference(segment[0])
                        .difference(segment[3])
                        .difference(segment[4])
                        .difference(segment[6]) for s in six_segment]
        segment[5] = set().union(*list(filter(lambda x: len(x) == 1, six_segment)))
        segment[2] = segment[2].difference(segment[5])

        # print(segment)
        output_value = 0
        for each in output.split(" "):
            if len(each) == 2:
                val = 1
            elif len(each) == 3:
                val = 7
            elif len(each) == 4:
                val = 4
            elif len(each) == 7:
                val = 8
            elif len(each) == 5:
                if not segment[4].intersection(set(each)):
                    if not segment[1].intersection(set(each)):
                        val = 3
                    else:
                        val = 5
                else:
                    val = 2
            elif len(each) == 6:
                if not segment[3].intersection(set(each)):
                    val = 0
                elif not segment[2].intersection(set(each)):
                    val = 6
                elif not segment[4].intersection(set(each)):
                    val = 9
            output_value = output_value * 10 + val
        print(output_value)
        total += output_value
    print(total)




def letters_from(l):
    result = []
    for code in l:
        for letter in code:
            if letter not in result:
                result.append(letter)
    result.sort()
    return set(result)

if __name__ == '__main__':
    main('input.txt')
