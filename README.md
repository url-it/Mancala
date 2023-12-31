# Mancala Game

This repository contains a Python implementation of the Mancala board game, along with several player strategies to play against each other. Mancala is a traditional game that involves capturing stones in pits on the board.

### How to Run

To play the game, execute the `main.py` script from the command line. You can specify a trace of moves as a command-line argument. The players are defined in the script and can be modified based on your preferences.

```bash
python main.py [trace]
```

trace: An optional argument representing a sequence of moves (e.g., "34521") to start the game.

### Game Rules

The game starts with a board configuration where each player has six pits and a store (pot). Players take turns choosing a pit on their side, and the stones in that pit are sown counterclockwise into the following pits. If the last stone is dropped into the player's pot, they get an extra turn. If the last stone lands in an empty pit on the player's side, and the opposite pit has stones, the player captures both the last stone and the stones in the opposite pit, placing them in their pot.

The game ends when a player's side is empty, and the remaining stones on the opponent's side are captured. The player with the most stones in their pot at the end wins.

### Players

Several player strategies are implemented:

manual: A human player that prompts the user for input.
random: A player that selects a random valid move.
PlayerMM: A player using the minimax algorithm with a specified search depth.
PlayerAB: A player using the alpha-beta pruning algorithm with a specified search depth.
PlayerDP: A player that caches and reuses heuristic scores to optimize performance.
TestPlayer: A customizable player with a user-defined heuristic.
Example
python
Copy code

### Create players

p1 = PlayerAB(1)
p2 = PlayerMM(2)

### Initialize the game with an optional trace

g = Game(trace, p1, p2)

### Run the game

g.runGame()
Note
This implementation uses Python 3.
Make sure to install any required dependencies using pip install [package]. The board printed to the console (Shown below) is colored using the termcolor package.
Feel free to explore and modify the code to experiment with different player strategies or game configurations. Enjoy playing Mancala!

```bash
Player 1 is thinking
   4 4 4 4 4 4
0                 1
   4 4 0 5 5 5
```
