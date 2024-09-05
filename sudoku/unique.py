import json
import time

try:
    with open("puzzles.json", "r") as f:
        puzzles = json.load(f)
except (FileNotFoundError, json.decoder.JSONDecodeError):
    puzzles = {
        "easy": [],
        "med": [],
        "hard": [],
        "evil": []
    }

valid_perms = []

def create_permutations() -> list:
    global valid_perms
    if len(valid_perms) > 0:
        return valid_perms
    
    state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = 0
    m = 9*8*7*6*5*4*3*2*1
    while l < m:
        for x in range(8, -1, -1):
            state[x] += 1
            if state[x] > 8:
                state[x] = 0
            else:
                break
        if len(set(state)) == 9:
            valid_perms.append(state[:])
            l += 1
            yield state
    
    return


def flip_horizontal(b: str) -> str:
    return b[ 8] + b[ 7] + b[ 6] + b[ 5] + b[ 4] + b[ 3] + b[ 2] + b[ 1] + b[ 0] + \
           b[17] + b[16] + b[15] + b[14] + b[13] + b[12] + b[11] + b[10] + b[ 9] + \
           b[26] + b[25] + b[24] + b[23] + b[22] + b[21] + b[20] + b[19] + b[18] + \
           b[35] + b[34] + b[33] + b[32] + b[31] + b[30] + b[29] + b[28] + b[27] + \
           b[44] + b[43] + b[42] + b[41] + b[40] + b[39] + b[38] + b[37] + b[36] + \
           b[53] + b[52] + b[51] + b[50] + b[49] + b[48] + b[47] + b[46] + b[45] + \
           b[62] + b[61] + b[60] + b[59] + b[58] + b[57] + b[56] + b[55] + b[54] + \
           b[71] + b[70] + b[69] + b[68] + b[67] + b[66] + b[65] + b[64] + b[63] + \
           b[80] + b[79] + b[78] + b[77] + b[76] + b[75] + b[74] + b[73] + b[72]


def flip_vertical(b: str) -> str:
    return b[72] + b[73] + b[74] + b[75] + b[76] + b[77] + b[78] + b[79] + b[80] + \
           b[63] + b[64] + b[65] + b[66] + b[67] + b[68] + b[69] + b[70] + b[71] + \
           b[54] + b[55] + b[56] + b[57] + b[58] + b[59] + b[60] + b[61] + b[62] + \
           b[45] + b[46] + b[47] + b[48] + b[49] + b[50] + b[51] + b[52] + b[53] + \
           b[36] + b[37] + b[38] + b[39] + b[40] + b[41] + b[42] + b[43] + b[44] + \
           b[27] + b[28] + b[29] + b[30] + b[31] + b[32] + b[33] + b[34] + b[35] + \
           b[18] + b[19] + b[20] + b[21] + b[22] + b[23] + b[24] + b[25] + b[26] + \
           b[ 9] + b[10] + b[11] + b[12] + b[13] + b[14] + b[15] + b[16] + b[17] + \
           b[ 0] + b[ 1] + b[ 2] + b[ 3] + b[ 4] + b[ 5] + b[ 6] + b[ 7] + b[ 8]


def rotate(b: str) -> str:
    return b[72] + b[63] + b[54] + b[45] + b[36] + b[27] + b[18] + b[ 9] + b[ 0] + \
           b[73] + b[64] + b[55] + b[46] + b[37] + b[28] + b[19] + b[10] + b[ 1] + \
           b[74] + b[65] + b[56] + b[47] + b[38] + b[29] + b[20] + b[11] + b[ 2] + \
           b[75] + b[66] + b[57] + b[48] + b[39] + b[30] + b[21] + b[12] + b[ 3] + \
           b[76] + b[67] + b[58] + b[49] + b[40] + b[31] + b[22] + b[13] + b[ 4] + \
           b[77] + b[68] + b[59] + b[50] + b[41] + b[32] + b[23] + b[14] + b[ 5] + \
           b[78] + b[69] + b[60] + b[51] + b[42] + b[33] + b[24] + b[15] + b[ 6] + \
           b[79] + b[70] + b[61] + b[52] + b[43] + b[34] + b[25] + b[16] + b[ 7] + \
           b[80] + b[71] + b[62] + b[53] + b[44] + b[35] + b[26] + b[17] + b[ 8]


def shift_row(b: str) -> str:
    return b[54] + b[55] + b[56] + b[57] + b[58] + b[59] + b[60] + b[61] + b[62] + \
           b[63] + b[64] + b[65] + b[66] + b[67] + b[68] + b[69] + b[70] + b[71] + \
           b[72] + b[73] + b[74] + b[75] + b[76] + b[77] + b[78] + b[79] + b[80] + \
           b[ 0] + b[ 1] + b[ 2] + b[ 3] + b[ 4] + b[ 5] + b[ 6] + b[ 7] + b[ 8] + \
           b[ 9] + b[10] + b[11] + b[12] + b[13] + b[14] + b[15] + b[16] + b[17] + \
           b[18] + b[19] + b[20] + b[21] + b[22] + b[23] + b[24] + b[25] + b[26] + \
           b[27] + b[28] + b[29] + b[30] + b[31] + b[32] + b[33] + b[34] + b[35] + \
           b[36] + b[37] + b[38] + b[39] + b[40] + b[41] + b[42] + b[43] + b[44] + \
           b[45] + b[46] + b[47] + b[48] + b[49] + b[50] + b[51] + b[52] + b[53]
           

def shift_col(b: str) -> str:
    return b[ 6] + b[ 7] + b[ 8] + b[ 0] + b[ 1] + b[ 2] + b[ 3] + b[ 4] + b[ 5] + \
           b[15] + b[16] + b[17] + b[ 9] + b[10] + b[11] + b[12] + b[13] + b[14] + \
           b[24] + b[25] + b[26] + b[18] + b[19] + b[20] + b[21] + b[22] + b[23] + \
           b[33] + b[34] + b[35] + b[27] + b[28] + b[29] + b[30] + b[31] + b[32] + \
           b[42] + b[43] + b[44] + b[36] + b[37] + b[38] + b[39] + b[40] + b[41] + \
           b[51] + b[52] + b[53] + b[45] + b[46] + b[47] + b[48] + b[49] + b[50] + \
           b[60] + b[61] + b[62] + b[54] + b[55] + b[56] + b[57] + b[58] + b[59] + \
           b[69] + b[70] + b[71] + b[63] + b[64] + b[65] + b[66] + b[67] + b[68] + \
           b[78] + b[79] + b[80] + b[72] + b[73] + b[74] + b[75] + b[76] + b[77]

def swap_row(b: str) -> str:
    return b[27] + b[28] + b[29] + b[30] + b[31] + b[32] + b[33] + b[34] + b[35] + \
           b[36] + b[37] + b[38] + b[39] + b[40] + b[41] + b[42] + b[43] + b[44] + \
           b[45] + b[46] + b[47] + b[48] + b[49] + b[50] + b[51] + b[52] + b[53] + \
           b[ 0] + b[ 1] + b[ 2] + b[ 3] + b[ 4] + b[ 5] + b[ 6] + b[ 7] + b[ 8] + \
           b[ 9] + b[10] + b[11] + b[12] + b[13] + b[14] + b[15] + b[16] + b[17] + \
           b[18] + b[19] + b[20] + b[21] + b[22] + b[23] + b[24] + b[25] + b[26] + \
           b[54] + b[55] + b[56] + b[57] + b[58] + b[59] + b[60] + b[61] + b[62] + \
           b[63] + b[64] + b[65] + b[66] + b[67] + b[68] + b[69] + b[70] + b[71] + \
           b[72] + b[73] + b[74] + b[75] + b[76] + b[77] + b[78] + b[79] + b[80]

def swap_col(b: str) -> str:
    return b[ 3] + b[ 4] + b[ 5] + b[ 0] + b[ 1] + b[ 2] + b[ 6] + b[ 7] + b[ 8] + \
           b[12] + b[13] + b[14] + b[ 9] + b[10] + b[11] + b[15] + b[16] + b[17] + \
           b[21] + b[22] + b[23] + b[18] + b[19] + b[20] + b[24] + b[25] + b[26] + \
           b[30] + b[31] + b[32] + b[27] + b[28] + b[29] + b[33] + b[34] + b[35] + \
           b[39] + b[40] + b[41] + b[36] + b[37] + b[38] + b[42] + b[43] + b[44] + \
           b[48] + b[49] + b[50] + b[45] + b[46] + b[47] + b[51] + b[52] + b[53] + \
           b[57] + b[58] + b[59] + b[54] + b[55] + b[56] + b[60] + b[61] + b[62] + \
           b[66] + b[67] + b[68] + b[63] + b[64] + b[65] + b[69] + b[70] + b[71] + \
           b[75] + b[76] + b[77] + b[72] + b[73] + b[74] + b[78] + b[79] + b[80]

def test_board(b: str, difficulty: str) -> (bool, str):
    "Will return true if the board is unique"
    board = "" # Scoping
    for state in create_permutations():
        board = b.translate(str.maketrans({
            str(state[0] + 1): "A",
            str(state[1] + 1): "B",
            str(state[2] + 1): "C",
            str(state[3] + 1): "D",
            str(state[4] + 1): "E",
            str(state[5] + 1): "F",
            str(state[6] + 1): "G",
            str(state[7] + 1): "H",
            str(state[8] + 1): "I",
        }))
        print(board)
        for flip in range(2):
            board = flip_vertical(board)
            for flop in range(2):
                board = flip_horizontal(board)
                for rot in range(4):
                    board = rotate(board)
                    for swip in range(3):
                        board = swap_col(board)
                        for swap in range(3):
                            board = swap_row(board)
                            for switch in range(2):
                                board = swap_col(board)
                                for swotch in range(2):
                                    board = swap_row(board)
                                    if board in puzzles[difficulty]:
                                        return False, board

    return True, board

def save_board(b: str, difficulty: str) -> bool:
    unique, board = test_board(b, difficulty)
    if not unique:
        return False

    puzzles[difficulty].append(board)
    with open("puzzles.json", "w") as f:
        json.dump(puzzles, f, indent = 4)

    return True


if __name__ == "__main__":
    t = time.time()
    unique = save_board("8.2..5.4.5.4.9..679.673...54...163..68.3.9.21..347...62...437.934..8.6.2.5.6..8.4", "easy")
    print(time.time() - t)
    print("Unique:", unique)