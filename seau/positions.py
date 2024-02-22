from typing import Literal


x_offset, y_offset, w_offset, h_offset = (0, 0, 0, 0)


def adjusted_rect_values(position: tuple[int, int, int, int]):
    x, y, w, h = position

    return (x + x_offset, y + y_offset, w + w_offset, h + h_offset)


type Positions = Literal["read_right_prompt", "read_query"]

positions: dict[Positions, tuple[int, int, int, int]] = {
    "read_right_prompt": adjusted_rect_values((959, 145, 944, 341)),
    "read_query": adjusted_rect_values((67, 332, 782, 37)),
}
