# Game of Life Kata

*See [Notes for evaluation](#notes-for-evaluation) if you are doing this kata as an evaluation.*

## Milestone 0: Graphical interface for input file generation toad.life

https://github.com/Ignat99/Generator_Game_of_Life

## Milestone 1: Game of life implementation

### Background
The universe of the [Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) is a two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, alive or dead, or "populated" or "unpopulated". Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

- Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
- Any live cell with two or three live neighbours lives on to the next generation.
- Any live cell with more than three live neighbours dies, as if by overpopulation.
- Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

The initial pattern constitutes the seed of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed—births and deaths occur simultaneously, and the discrete moment at which this happens is sometimes called a tick (in other words, each generation is a pure function of the preceding one). The rules continue to be applied repeatedly to create further generations.

Game of life patterns are represented by ASCII files containing any number of rows starting with `!` that can be ignored, then the universe state represented as `.` for dead cells and `O` for live cells.

### Acceptance criteria
- The program `gameoflife` should read a game of life pattern from standard input, increment the state one generation, and write the resulting pattern to standard output.
- The four rules in [Background](#background) must be respected.
- `gameoflife` should return a nonzero exit status if the game file is invalid.

### Hints
- Make sure you have enough coverage of edge cases - where there are births and deaths at the edge of the grid.
- Here is how an example usage of `gameoflife` should look:
```
$ cat patterns/toad.life
!Name: Toad
!
......
......
..OOO.
.OOO..
......
......

$ cat patterns/toad.life | ./gameoflife.py
......
...O..
.O..O.
.O..O.
..O...
......

$ cat patterns/toad.life | ./gameoflife.py | ./gameoflife.py
......
......
..OOO.
.OOO..
......
......

```

## Milestone 2: Game variations

### Background
[Rulestrings](https://www.conwaylife.com/wiki/Rulestring) permit customizations of rules in the game.
In our case, we will use the *B/S notation* to define rules:

>  `B{number list}/S{number list}`.  B (for birth) is a list of all the numbers of live neighbors that cause a dead cell to come alive (be born); S (for survival) is a list of all the numbers of live neighbors that cause a live cell to remain alive (survive).

For example, the version we already implemented has the rulestring `B3/S23`.

This new modification implies a change in the input of our program.

### Acceptance criteria

- The program `gameoflife` now requires one input argument, the rulestring.
- The program increments the state according to the variation of the rulestring.
- The program returns a nonzero exit status if the rulestring is not well-formed.

### Example
```
$ cat patterns/cross.life
!Name: cross
!
.....
..O..
.OOO.
..O..
.....

$ cat patterns/cross.life | ./gameoflife.py B368/S245
.....
.O.O.
..O..
.O.O.
.....

$ cat patterns/cross.life | ./gameoflife.py B368/S245 | ./gameoflife B368/S245
.....
..O..
.OOO.
..O..
.....
```


## Milestone 3: Infinite grid

### Background
For previous milestones, the game universe was bounded. Now, we want to it to wrap on all edges, creating a toroidal topology.

### Acceptance criteria
- The state is calculated giving every cell 8 neighbors. Cells on the edge consider cells on the opposite edge to be neighbors.

## Milestone 4

The idea for this step is to avoid some bad practices and keep clean code. To do this, we have made a list of mandatory constraints to follow as an exercise (some of them can not be applied).

#### No primitives across method boundaries

The constraint “No primitives across method boundaries” means that, separate from the constructor (which isn’t really a ‘normal’ method), you cannot have a method that returns or is passed a primitive (int, string etc.). You have to use objects. So this way you’re forced to take the Primitive Obsession code smell seriously, and use more objects.

#### No conditional statements:

- No ifs, no switch, no loops for conditional. The alternatives are polymorphism and hashtables
- Conditional statements are a form of primitive obsession (we tend to use the lowest level of abstraction instead of choosing a higher level). For example, we may choose an int for an employee number instead of an employee number class.

#### Immutable can be simpler than mutable

#### Polymorphism to control state

#### Only four lines per method


## Extra possible activities
- Change partner every 10 mins
- Ping Pong: One person writes the test, the other implements the test.
- Taking baby steps. 5 mins write code, 5 mins test and 5 mins refactor, if they don't finish before the timer goes off they have to delete and start over.


## Notes for evaluation
You can choose the language that you prefer.

Please tag the commit in which you accomplish each milestone.

Keep in mind:
- Tests and coverage.
- Good design and naming.
- Documentation.
- The story told by the commit history.
- The standards and conventions of the language you choose.

 Consider including:
- Decision and design document (it can be small).
- Installation and execution instructions.

### Language-specific notes
- If you choose **Python**, please use type annotations.
