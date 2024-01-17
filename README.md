# Icebreaker Game

Overview
This game is a two-player turn-based strategy game called "Icebreaker." The players take turns moving their characters on an 8x8 game board, breaking ice squares, and trying to outmaneuver their opponent. The game includes a graphical user interface (GUI) implemented using the Graphics library.


Game Rules
1. Each player controls a character represented by a coloured circle: Player 1 (red) and Player 2 (blue).
2. Players take turns moving to adjacent squares on the 8x8 game board.
3. After moving, a player can choose to break an ice square.
4. Breaking ice is allowed only under certain conditions, such as the square being ice and not previously broken and a player cannot be on the ice.
5. The game continues until one player is unable to make a legal move.
6. The player that still has legal moves wins the round.


Program Structure and Game Logic
The program consists of four main classes: Board, Player, SplashScreen, and ScoreScreen. The game's main logic is implemented in the main() function.

Board Class
__init__(self, win): Initializes the game board, players, and other variables.
getSquare(self, x, y): Returns the graphical representation of a square on the board.
breakIce(self, x, y, player1, player2): Attempts to break ice at the specified coordinates during a turn.
is_valid_move(self, player, new_x, new_y, player1, player2): Checks if a move is valid for a player.
Other helper functions for game logic, such as legalBreak, isBroken, switchPlayer, etc.

Player Class
__init__(self, win, clr, start_x, start_y): Initializes a player with a colour and starting position.
move(self, new_x, new_y): Moves the player to a new position on the board.

SplashScreen Class
__init__(self): Displays a splash screen with the game title and buttons to play or quit.
get_choice(self): Waits for the user to click either the "Play" or "Quit" button and returns the choice.

ScoreScreen Class
__init__(self, winner, points): Displays the score screen when a player wins a round.
get_choice(self): Waits for the user to click either the "Play Again" or "Quit" button and returns the choice.

main() Function
Initializes the game by creating instances of the SplashScreen, Board, and player classes.
Implements the game loop, allowing players to take turns, make moves, and break ice.
Displays status information, coordinates, and buttons for quitting or resetting the game.
Handles user input, updates the GUI, and determines the winner of each round.


Program Constants
Window Width: Width of the game window (400 pixels).
Window Height: Height of the game window (500 pixels).


Global Variables
No global variables.


Function Names and Descriptions
Board Class
__init__(self, win): Initializes the game board and other variables.
getSquare(self, x, y): Returns the graphical representation of a square on the board.
breakIce(self, x, y, player1, player2): Attempts to break ice at the specified coordinates during a turn.
is_valid_move(self, player, new_x, new_y, player1, player2): Checks if a move is valid for a player.
switchPlayer(self): Switches the turn to the other player.
reset(self, player1, player2): Resets the game state to the initial state.
legal_move_exists(self, player1, player2): Checks if there is at least one legal move available for the current player.
detect_winner(self, player1, player2): Determines the winner of the current round based on legal moves.

Player Class
__init__(self, win, clr, start_x, start_y): Initializes a player with a colour and starting position.
move(self, new_x, new_y): Moves the player to a new position on the board.

SplashScreen Class
__init__(self): Initializes the splash screen.
get_choice(self): Waits for the user to click either the "Play" or "Quit" button and returns the choice.

ScoreScreen Class
__init__(self, winner, points): Initializes the score screen.
get_choice(self): Waits for the user to click either the "Play Again" or "Quit" button and returns the choice.

main() Function
main(): The main function to start the game, handle user input, and implement the game loop.
