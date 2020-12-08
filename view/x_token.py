from view.token_piece import TokenPiece


class XToken(TokenPiece):
    def draw_token(self, line: int) -> str:
        if line == 0:
            return r"  \\  //  "
        elif line == 1:
            return "    xx    "
        elif line == 2:
            return r"  //  \\  "

    def __str__(self):
        return "X"

    def is_token(self, response: str):
        return response in ["x", "X"]
