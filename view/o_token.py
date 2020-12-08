from view.token_piece import TokenPiece


class OToken(TokenPiece):
    def draw_token(self, line: int) -> str:
        if line == 0:
            return r"  //==\\  "
        elif line == 1:
            return "  ||  ||  "
        elif line == 2:
            return r"  \\==//  "

    def __str__(self):
        return "O"

    def is_token(self, response: str):
        return response in ["o", "O", "0"]
