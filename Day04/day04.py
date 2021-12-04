def earliest_win(card):
    wins_at = max(card[0])
    for row_number in range(1,5):
        highest_in_row = max(card[row_number])
        if highest_in_row < wins_at:
            wins_at = highest_in_row

    for column_number in range(5):
        highest_in_column = max([row[column_number] for row in card])
        if highest_in_column < wins_at:
            wins_at = highest_in_column
    return wins_at


def read_card(f, called_numbers):
    rows = []
    for i in range(5):
        rows.append([called_numbers.index(int(spot))
            for spot in f.readline().split()])
    return rows

def read_boards(file_name):
    cards = []
    with open(file_name, "r") as f:
        called_numbers = list(map(int, f.readline().split(sep=',')))

        while f.readline():
            cards.append(read_card(f, called_numbers))
    return (called_numbers, cards)


def part1(called_numbers, cards):
    first_win = len(called_numbers)
    winning_card = None
    for card in cards:
        win = earliest_win(card)
        if win < first_win:
            first_win = win
            winning_card = card

    score = called_numbers[first_win] *\
            sum([called_numbers[spot]
                 for row in winning_card
                 for spot in row if spot > first_win])
    print(score)

def part2(called_numbers, cards):
    last_win = 0
    winning_card = None
    for card in cards:
        win = earliest_win(card)
        if win > last_win:
            last_win = win
            winning_card = card

    score = called_numbers[last_win] *\
            sum([called_numbers[spot]
                 for row in winning_card
                 for spot in row if spot > last_win])
    print(score)


if __name__ == '__main__':
    (callled_numbers, cards) = read_boards("input.txt")
    part1(callled_numbers, cards)
    part2(callled_numbers, cards)
