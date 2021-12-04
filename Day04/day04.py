def earliest_win(card):
    wins_at = [max(row) for row in card]
    wins_at.extend([max([row[column_number] for row in card]) for column_number in range(5)])
    turn = min(wins_at)
    return turn


def read_card(f, called_numbers):
    return [[called_numbers.index(int(spot))
                     for spot in f.readline().split()] for i in range(5)]


def read_boards(file_name):
    bingo_cards = []
    with open(file_name, "r") as f:
        called_numbers = list(map(int, f.readline().split(sep=',')))

        while f.readline():
            bingo_cards.append(read_card(f, called_numbers))
    return called_numbers, bingo_cards


def part1(called_numbers, bingo_cards):
    first_win, winning_card = min([(earliest_win(card), card) for card in bingo_cards])

    score = called_numbers[first_win] * sum(
        [called_numbers[spot] for row in winning_card for spot in row if spot > first_win])
    print(score)


def part2(called_numbers, bingo_cards):
    last_win, winning_card = max([(earliest_win(card), card) for card in bingo_cards])

    score = called_numbers[last_win] * sum(
        [called_numbers[spot] for row in winning_card for spot in row if spot > last_win])
    print(score)


if __name__ == '__main__':
    (numbers, cards) = read_boards("input.txt")
    part1(numbers, cards)
    part2(numbers, cards)
