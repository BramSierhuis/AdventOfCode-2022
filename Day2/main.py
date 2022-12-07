rock_value = 1
paper_value = 2
scissors_value = 3

lose_value = 0
win_value = 6
draw_value = 3

rock = "A"
paper = "B"
scissors = "C"

lose = "X"
draw = "Y"
win = "Z"


def get_score(move, response):
    score = 0

    if move == rock:
        if response == lose:
            score += lose_value + scissors_value
        elif response == draw:
            score += draw_value + rock_value
        else:
            score += win_value + paper_value

    elif move == scissors:
        if response == lose:
            score += lose_value + paper_value
        elif response == draw:
            score += draw_value + scissors_value
        else:
            score += win_value + rock_value

    else:
        if response == lose:
            score += lose_value + rock_value
        elif response == draw:
            score += draw_value + paper_value
        else:
            score += win_value + scissors_value

    return score


with open("../Day2/input.txt") as file_in:
    total_score = 0

    for line in file_in:
        inputs = line.strip('\n').split(" ")

        total_score += get_score(inputs[0], inputs[1])

print(total_score)
