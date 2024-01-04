# Mancala Game With AI

## What is Mancala?

Mancala is a game involving two players taking turns collecting the most pieces, usually stones, in their "stores" at the opposite ends of the board. The physical Mancala board has two six-pocket rows with four pieces in each, also known as stones, and two stores, which don't have anything in them.

![alt text](https://media.springernature.com/lw685/springer-static/image/chp%3A10.1007%2F978-3-031-34017-8_1/MediaObjects/541501_1_En_1_Fig1_HTML.png)

The board should look like this in the terminal:
```bash
Player 1 is thinking
   4 4 4 4 4 4
0                 1
   4 4 0 5 5 5
```

### Rules

1. In each turn of the game, a player picks up all the pieces in a pit and moves counter-clockwise, placing one stone in each pocket until the stones are exhausted. If the player passes their store during this process, they also deposit one stone in it. However, the player skips over the opponent's store.
2. The last piece a player places lands in their store, they get an extra turn.
4. If the last piece a player places is in an empty space on their side, and the opponent has stones in the pit exactly opposite to this empty space, the player collects all the stones in the opponent's opposite pit, in addition to their last placed stone.
5. The game concludes when all the stones on one side of the board are depleted. At this point, the remaining player gathers all the stones on their side and places them in their store.
6. Finally, the player with the most stones is a winner.

Usually, this game requires two players, but we can also play with one player and one AI. The game includes various AI strategies like minimax, dynamic programming, base player, and alpha-beta pruning. The many AI options add complexity to the gameplay, offering different levels of challenge for players, depending on the layers you allow it to have.

## AI Options

The game includes several AI strategies that provide different levels of difficulty for players:

- **Minimax Algorithm (`playerMM`):** This player utilizes the minimax algorithm with a specified search depth to make strategic moves.
 
- **Alpha-Beta Pruning (`playerAB`):** This player employs the alpha-beta pruning algorithm with a specified search depth for more efficient decision-making.

- **Dynamic Programming (`playerDP`):** This player caches and reuses heuristic scores to optimize performance and speed up decision-making.

- **Random Move (`random`):** This player selects a random valid move, offering a less predictable opponent.

- **Customizable Heuristic (`testPlayer`):** This player allows users to define their own heuristic, providing flexibility for experimentation.

Also note that there are some AIs that require a depth limit referring to the max they can go down a tree, example provided below, as to predicting the best moves possible. I would suggest learning more about the Minimax and Alpha-Beta throught this [link](https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/).
![alt text](https://media.geeksforgeeks.org/wp-content/uploads/MIN_MAX1.jpg)

## How to Play

To play I would suggest cloning this repository and storing it in your preferred location. To clone:
 ```bash
 git clone https://github.com/url-it/Mancala.git
 cd mancala-game
```
Since this is a terminal game all you need to do is just run the game via python3 or python depending on your system, for macOS it would be python3 for python 3 versions.
```bash
python3 Game.py
```

Something to note is that you can chnage the different AIs in the [Game.py](Game.py) file, as stated, you can choose from the various options from the AI options. 
I have included a comments of the different AI options just in case, but of course you can check them out in the [player.py](player.py) file, as well as how they work.
```python3
   if len(sys.argv) >= 2:
        trace = sys.argv[1]
    else:
        trace = ""

   #Players you can set it to. 
    p1 = playerAB(5)
    p2 = manual()
    g = Game(trace, p1, p2)
    g.runGame()

```

## Final Note
The implementation is designed for Python 3. Install any required dependencies using pip install [package]. Feel free to explore and modify the code to experiment with different player strategies or game configurations. Feedback would be greatly appreciated as I would like to move an actual UI instead of leaving it as terminal, and improving anything on the algorithms used. Enjoy playing Mancala!

