from typing import Literal


x_offset, y_offset, w_offset, h_offset = (0, 0, 0, 0)


def adjusted_rect_values(position: tuple[int, int, int, int]):
    x, y, w, h = position

    return (x + x_offset, y + y_offset, w + w_offset, h + h_offset)


def adjusted_coordinates(position: tuple[int, int]):
    x, y = position

    return (x + x_offset, y + y_offset)


type Positions = Literal[
    "dissatisfaction_likely",
    "dissatisfaction_possible",
    "neutral",
    "satisfaction_possible",
    "satisfaction_likely",
    "read_query",
]

positions: dict[Positions, tuple[int, int] | tuple[int, int, int, int]] = {
    "dissatisfaction_likely": adjusted_coordinates((99, 500)),
    "dissatisfaction_possible": adjusted_coordinates((236, 500)),
    "neutral": adjusted_coordinates((375, 500)),
    "satisfaction_possible": adjusted_coordinates((513, 500)),
    "satisfaction_likely": adjusted_coordinates((650, 500)),
    "read_query": adjusted_rect_values((25, 242, 1476, 122)),
}
