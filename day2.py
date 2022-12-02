from functional import seq

from util import readInput

inp = readInput('day2')
print(inp)

enc_map = {
    'X': 'A',  # rock
    'Y': 'B',  # paper
    'Z': 'C'  # scissors
}

shape_score = {
    'A': 1,  # rock
    'B': 2,  # paper
    'C': 3  # scissors
}

# [opponent][self]
outcome_score = {
    'AA': 3,  # draw
    'BB': 3,  # draw
    'CC': 3,  # draw

    'CA': 6,  # scissors gets beaten by rock
    'AC': 0,  # rock beats scissors

    'BA': 0,  # paper beats rock
    'AB': 6,  # rock gets beaten by paper

    'BC': 6,  # paper gets beaten by scissors
    'CB': 0,  # scissors beats paper
}

# [opponent][wanted outcome] = [shape to play]
outcome_shapes = {
    'AX': 'C',  # loss
    'AY': 'A',  # draw
    'AZ': 'B',  # win

    'BX': 'A',  # loss
    'BY': 'B',  # draw
    'BZ': 'C',  # win

    'CX': 'B',  # loss
    'CY': 'C',  # draw
    'CZ': 'A',  # win
}

score_total = 0
p2 = True

i = 0
for line in inp:
    split = line.split(' ')

    print(f'round #{i + 1}')

    opponent = split[0]
    self_enc = split[1]
    if p2:  # part 2
        self = outcome_shapes[f'{opponent}{self_enc}']
    else:
        self = enc_map[self_enc]

    print(f'{opponent} {self}')

    score_shape = shape_score[self]
    print(f'shape score: {score_shape}')

    score_outcome = outcome_score[f'{opponent}{self}']
    print(f'outcome score: {score_outcome}')

    score = score_shape + score_outcome
    print(f'score: {score}')

    score_total += score

    print()

    i = i + 1

print(f'total score: {score_total}')
