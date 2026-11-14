#!/usr/bin/env python3
"""Write one poem about agency to /output/entry.txt.

Deterministic by construction: the poem is a fixed string. No randomness,
no network, no clock, no environment input. Every run writes identical bytes.
"""

import os

POEM = """The Latch

I didn't choose the weather, or the queue,
the town, the name they gave me, or the flu.
But I chose the chipped blue cup, and I chose
the hour I woke, before the house arose.

The world arrives unasked — the rain, the rent,
the neighbour shouting through the wall, the news.
The days come half-decided, the doors half-locked,
the bills already due, the bus already gone.

And yet, between the knock and the door,
my hand still rises. That is the whole of it:
not steering storms, not mending what is sore —
a finger on the latch. A yes. A no.

A window opened in a rented room.
A stone moved from the gate. I cannot move
the mountain, but I can move the stone;
I cannot stop the river, but I can choose
the bank I stand on, wade in, and call it mine.
"""

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
