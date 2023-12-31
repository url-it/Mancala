# Mancala Game With AI

## What is Mancala?

Mancala is a game involving two players taking turns collecting the most pieces, usually stones, in their "stores" at the opposite ends of the board. The physical Mancala board has two six-pocket rows with four pieces in each, also known as stones, and two stores, which don't have anything in them.

![alt text](https://media.springernature.com/lw685/springer-static/image/chp%3A10.1007%2F978-3-031-34017-8_1/MediaObjects/541501_1_En_1_Fig1_HTML.png)

### Rules

1. In each turn of the game, a player picks up all the pieces in a pit and moves counter-clockwise, placing one stone in each pocket until the stones are exhausted. If the player passes their store during this process, they also deposit one stone in it. However, the player skips over the opponent's store.
2. The last piece a player places lands in their store, they get an extra turn.
4. If the last piece a player places is in an empty space on their side, and the opponent has stones in the pit exactly opposite to this empty space, the player collects all the stones in the opponent's opposite pit, in addition to their last placed stone.
5. The game concludes when all the stones on one side of the board are depleted. At this point, the remaining player gathers all the stones on their side and places them in their store.
6. Finally, the player with the most stones is a winner.

Usually, this game requires two players, but we can also play with one player and one AI. The game includes various AI strategies like minimax, dynamic programming, base player, and alpha-beta pruning. The many AI options add complexity to the gameplay, offering different levels of challenge for players, depending on the layers you allow it to have.


```bash
Player 1 is thinking
   4 4 4 4 4 4
0                 1
   4 4 0 5 5 5
```
