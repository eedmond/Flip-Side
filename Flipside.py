import itertools


# Represents the game of FlipSide. Defaults to a "solution" and exposes
# functions to execute moves. A move is defined as two flips because
# this is the minimum action you can do with the game.
class FlipSide:
    def __init__(self):
        self.top_row = [x for x in range(5)]
        self.bottom_row = [x for x in range(5, 10)]

    def swap_individual(self, top_pos, bottom_pos):
        self.top_row[top_pos], self.bottom_row[bottom_pos] = (
            self.bottom_row[bottom_pos],
            self.top_row[top_pos],
        )

    def execute_move(self, top_pos_1, bottom_pos_1, top_pos_2, bottom_pos_2):
        assert (
            0 <= top_pos_1 <= 2
            and 0 <= bottom_pos_1 <= 2
            and 0 <= top_pos_2 <= 2
            and 0 <= bottom_pos_2 <= 2
        )
        for i in range(3):
            self.swap_individual(top_pos_1 + i, bottom_pos_1 + i)
        for i in range(3):
            self.swap_individual(top_pos_2 + i, bottom_pos_2 + i)

    # Returns a formatted string for the given row with '*' replacing the
    # value if the value is unchanged from the initial position.
    def __get_row_debug_string(self, row, initial_index):
        return "".join(
            [
                str(val) if index + initial_index != val else "*"
                for index, val in enumerate(row)
            ]
        )

    def top_row_debug_string(self):
        return self.__get_row_debug_string(self.top_row, 0)

    def bottom_row_debug_string(self):
        return self.__get_row_debug_string(self.bottom_row, len(self.top_row))


with open("single_move_output.txt", "w") as f:
    for move in itertools.product([0, 1, 2], repeat=4):
        if move[0] == move[2] and move[1] == move[3]:
            continue
        flip_side = FlipSide()
        flip_side.execute_move(move[0], move[1], move[2], move[3])
        f.write(
            "{}\t{}\t{}\n{}\t{}\t{}\n".format(
                move[0],
                move[2],
                flip_side.top_row_debug_string(),
                move[1],
                move[3],
                flip_side.bottom_row_debug_string(),
            )
        )
