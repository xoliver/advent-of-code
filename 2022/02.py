# SCORES[ME][OPPONENT]
SCORES = {
    "X": { # 1
        "A": 4,
        "B": 1,
        "C": 7,
    },
    "Y": { # 2
        "A": 8,
        "B": 5,
        "C": 2,
    },
    "Z": { # 3
        "A": 3,
        "B": 9,
        "C": 6,
    },
}

score = 0
with open("02.txt", "r") as f:
    for line in f.readlines():
        opponent, me = line.strip().split(" ")
        score += SCORES[me][opponent]

print("Part 1", score)

SCORES2 = {
    "A": { # Rock
        "X": 3, # Lose with scissors: 0+3
          "Y": 4, # Draw with rock: 3+1
          "Z": 8, # Win with paper: 6+2
    },
    "B": { # Paper
        "X": 1, # Lose with rock: 0+1
          "Y": 5, # Draw with paper: 3+2
          "Z": 9, # Win with scissors: 6+3
    },
     "C": { # Scissors
        "X": 2, # Lose with paper: 0+2
          "Y": 6, # Draw with scissors: 3+3
          "Z": 7, # Win with rock: 6+1
    },
}
score2 = 0
with open("02.txt", "r") as f:
    for line in f.readlines():
        opponent, me = line.strip().split(" ")
        score2 += SCORES2[opponent][me]

print("Part 2", score2)


