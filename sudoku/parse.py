import argparse
import unique

parser = argparse.ArgumentParser()
parser.add_argument(
    "difficulty", 
    type = str, 
    choices = ["easy", "med", "hard", "evil"]
)

args = parser.parse_args()
for line in open("boards.properties").read().split("\n"):
    if args.difficulty not in line:
        continue
    unique.save_board(line.split("=")[1].strip(), args.difficulty)