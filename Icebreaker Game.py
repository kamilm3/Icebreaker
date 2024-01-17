from Graphics import *


class Board:
    def __init__(self, win):
        """
        Purpose: Initializes the starting values and attributes of the class. Creates the board with 50x50 pixel per rectangle (Makes them white) and the rectangles make a 8x8 grid this is stored into a list. And then the self.ice is also stored into a list.
        Parameters: There is 1 main variable win and it is used to draw the board. And there is self which is used to access variables in the class.
        Return: None.
        """
        self.win = win
        self.turn = 0
        self.ice_broken_this_turn = (
            False  # New variable to track ice breaking during the current turn
        )
        self.current_action = "move"  # New variable to track the current action
        self.points = {"Player 1": 0, "Player 2": 0}  # Initialize points

        self.board = []
        for y in range(8):
            bLine = []
            for x in range(8):
                xPosn = x * 50
                yPosn = y * 50
                sqr = Rectangle(Point(xPosn, yPosn), Point(xPosn + 50, yPosn + 50))
                sqr.setFill("white")
                bLine.append(sqr)
                sqr.draw(win)
            self.board.append(bLine)

        self.ice = []
        for y in range(8):
            iLine = []
            for x in range(8):
                iLine.append(True)
            self.ice.append(iLine)

    def getSquare(self, x, y):
        """
        Purpose: Returns a rectangle and its y and x from the list self.board.
        Parameters: There are 2 main variables x and y, which are for the coordinates of the rectangle. And there is self which is used to access variables in the class.
        Return: It returns the y and x of the rectangle from self.board.
        """
        return self.board[y][x]

    def breakIce(self, x, y, player1, player2):
        """
        Purpose: This is to break the ice at a specific coordinate (x, y) during a game. The ice-breaking action is subject to certain conditions.
        Parameters: There are 4 main variables x, y, player1, and player2. These are for the coordinates for the ice sqaure that needs to be broken and information about the players. And there is self which is used to access variables in the class.
        Return: True if ice is broken. False if not.
        """
        if (
            self.current_action == "break"
            and not self.ice_broken_this_turn
            and self.legalBreak(x, y, player1, player2)
        ):
            self.ice[y][x] = False
            self.getSquare(x, y).setFill("skyblue2")
            self.ice_broken_this_turn = True
            self.current_action = "move"  # Switch to move after breaking ice
            self.switchPlayer()
            return True
        return False

    def isIce(self, x, y):
        """
        Purpose: Returns a rectangle and its y and x from the list self.ice.
        Parameters: There are 2 main variables x and y, which are for the coordinates of the rectangle. And there is self which is used to access variables in the class.
        Return: It returns the y and x of the rectangle from self.ice.
        """
        return self.ice[y][x]

    def movePlayer(self, player, new_x, new_y):
        """
        Purpose: Updates the players locations.
        Parameters: There are 3 main variables new_x and new_y and player, which are for the new coordinates for the player in the variable. And there is self which is used to access variables in the class.
        Return: None.
        """
        old_x, old_y = player.location
        player.location = (new_x, new_y)
        player.symbol.move((new_x - old_x) * 50, (new_y - old_y) * 50)

    def legalBreak(self, x, y, player1, player2):
        """
        Purpose: Check if breaking the ice at a specified coordinate is legal.
        Parameters: There are 4 main variables x, y, player1, and player2. These are for the coordinates for the ice sqaure that needs to be broken and information about the players. And there is self which is used to access variables in the class.
        Return: True if it is legal. False if not.
        """
        return (
            self.current_action == "break"
            and not self.ice_broken_this_turn
            and self.on_map(x, y)
            and self.isIce(x, y)
            and not self.isBroken(x, y)
            and not self.is_occupied(x, y, player1, player2)
        )

    def isBroken(self, x, y):
        """
        Purpose: Check if the ice at the specified position is already broken.
        Parameters: There are 2 main variables x, y. These are for the coordinates for the ice sqaure to check. And there is self which is used to access variables in the class.
        Return: True if the ice is broken. False if not.
        """
        return not self.ice[y][x]

    def switchPlayer(self):
        """
        Purpose: To switch the players turns.
        Parameters: There is self which is used to access variables in the class.
        Return: None.
        """
        self.turn = 1 - self.turn
        self.ice_broken_this_turn = False
        self.current_action = "move"  # Reset the action when switching players

    def on_map(self, x, y):
        """
        Purpose: To make sure the coordinates are on the 8x8 board that was created.
        Parameters: There are 2 main variables x and y, which are for the coordinates to see if it is on the 8x8 board. And there is self which is used to access variables in the class.
        Return: Boolean True or False
        """
        return 0 <= x < 8 and 0 <= y < 8

    def is_valid_move(self, player, new_x, new_y, player1, player2):
        """
        Purpose: Check if the specified move is valid for a player.
        Parameters: There are 5 main variables player, new_x, new_y, player1, player2. These are for the player that is being checked, coordinates of the intended new position for the player, information about the other players in the game. And there is self which is used to access variables in the class.
        Return: True if the move is valid. False if not.
        """
        old_x, old_y = player.location
        if (
            (abs(new_x - old_x) in {0, 1} and abs(new_y - old_y) in {0, 1})
            and self.on_map(new_x, new_y)
            and self.isIce(new_x, new_y)
            and not self.is_occupied(new_x, new_y, player1, player2)
        ):
            return True
        return False

    def is_occupied(self, x, y, player1, player2):
        """
        Purpose: Check if the square is occupied by any player.
        Parameters: There are 4 main variables x, y, player1, player2. These are for the coordinates of the square to check, and information about the players in the game. And there is self which is used to access variables in the class.
        Return: True if the square is occupied by any player. False if not.
        """
        if player1.location == (x, y) or player2.location == (x, y):
            return True
        return

    def reset(self, player1, player2):
        """
        Purpose: Reset the state of the game board and player positions to an initial state.
        Parameters: There are 2 main variables player1, player2. These are for the information about the players in the game. And there is self which is used to access variables in the class.
        Return: None.
        """
        for y in range(8):
            for x in range(8):
                self.ice[y][x] = True
                self.getSquare(x, y).setFill("white")

        player2.move(0, 0)
        player1.move(7, 7)
        player2.location = (0, 0)
        player1.location = (7, 7)
        self.turn = 0
        self.ice_broken_this_turn = False
        self.current_action = "move"
        self.points = {
            "Player 1": 0,
            "Player 2": 0,
        }  # Reset points when resetting the board

    def legal_move_exists(self, player1, player2):
        """
        Purpose: Check if there is at least one legal move available for the current player.
        Parameters: There are 2 main variables player1, player2. These are for the information about the players in the game. And there is self which is used to access variables in the class.
        Return: True if there is a legal move. False if not.
        """
        current_player = player1 if self.turn == 0 else player2

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                new_x, new_y = (
                    current_player.location[0] + dx,
                    current_player.location[1] + dy,
                )
                if self.is_valid_move(current_player, new_x, new_y, player1, player2):
                    return True
        return False

    def detect_winner(self, player1, player2):
        """
        Purpose: Determine the winner of the current round based on legal moves and update points.
        Parameters: There are 2 main variables player1, player2. These are for the information about the players in the game. And there is self which is used to access variables in the class.
        Return: Tuple. First element is True if there is a winner, False if not. Second element is winners name (Player 1 or Player 2) if there is a winner, None if not.
        """
        legal_move_current_player = self.legal_move_exists(player1, player2)
        legal_move_opponent = self.legal_move_exists(player2, player1)

        if not legal_move_current_player:
            winner = "Player 2" if self.turn == 1 else "Player 1"
        elif not legal_move_opponent:
            winner = "Player 1" if self.turn == 1 else "Player 2"
        else:
            return False, None  # No winner yet

        self.points[winner] += 1  # Update points for the winner
        return True, winner


class Player:
    def __init__(self, win, clr, start_x, start_y):
        """
        Purpose: Initializes the starting values and attributes of the class. Creates the players in a form of a circle with their color and draws them in their starting locations.
        Parameters: There are 4 main variables start_x and start_y, which are for the coordinates to place them on the board. Then there is clr which is for the color of the players and there is win to draw the players. And there is self which is used to access variables in the class.
        Return: None.
        """
        self.color = clr
        self.location = (start_x, start_y)
        self.symbol = Circle(Point(start_x * 50 + 25, start_y * 50 + 25), 20)
        self.symbol.setFill(clr)
        self.symbol.draw(win)

    def move(self, new_x, new_y):
        """
        Purpose: Gets the current location of the player. Then it updates the players location and moves the players symbol.
        Parameters: There are 3 main variables new_x and new_y and player, which are for the new coordinates for the player in the variable. And there is self which is used to access variables in the class.
        Return: None.
        """
        old_x, old_y = self.location
        self.location = (new_x, new_y)
        self.symbol.move((new_x - old_x) * 50, (new_y - old_y) * 50)


class SplashScreen:
    def __init__(self):
        """
        Purpose: Initializes the starting values and attributes of the class. This is a Spalsh Screen at the start when the game is launched. Has the name of the game with other details. There are Play and Quit buttons aswell.
        Parameters: There is self which is used to access variables in the class.
        Return: None
        """
        self.window = GraphWin(
            "Kamil Malkowski - Icebreaker Game Version 3.0 - 12/08/23", 400, 500
        )
        self.window.setBackground("skyblue2")

        # Title
        title_text = Text(Point(200, 150), "Icebreaker Game")
        title_text.setSize(20)
        title_text.setFace("courier")
        title_text.draw(self.window)

        # Name
        name_text = Text(Point(200, 175), "by Kamil Malkowski")
        name_text.setSize(15)
        name_text.setFace("courier")
        name_text.draw(self.window)

        # Play button
        play_button = Rectangle(Point(100, 230), Point(300, 300))
        play_button.setFill("chartreuse2")
        play_text = Text(Point(200, 265), "Play")
        play_text.setSize(17)
        play_text.setFace("courier")
        play_button.draw(self.window)
        play_text.draw(self.window)

        # Quit button
        quit_button = Rectangle(Point(100, 320), Point(300, 390))
        quit_button.setFill("orangered1")
        quit_text = Text(Point(200, 355), "Quit")
        quit_text.setSize(17)
        quit_text.setFace("courier")
        quit_button.draw(self.window)
        quit_text.draw(self.window)

    def get_choice(self):
        """
        Purpose: Get the user's choice (Play or Quit) based on mouse clicks in the game window.
        Parameters: There is self which is used to access variables in the class.
        Return: Str. Either "play" or "quit" depending on what the user clicks.
        """
        while True:
            click_point = self.window.checkMouse()
            if click_point is not None:
                x, y = int(click_point.getX()), int(click_point.getY())
                if 100 <= x <= 300 and 230 <= y <= 300:
                    return "play"
                elif 100 <= x <= 300 and 320 <= y <= 390:
                    return "quit"


class ScoreScreen:
    def __init__(self, winner, points):
        """
        Purpose: Initializes the starting values and attributes of the class. This is the Score screen when a player wins. It displays who won the current round and the current score of the game. It also has buttons "Play Again" or "Quit".
        Parameters: There is 2 main variables winner and points. winner is the name of the winner. And points is a dictionary containing the points for each player. And there is self which is used to access variables in the class.
        Return: None.
        """
        self.window = GraphWin("Score Screen", 300, 200)
        self.window.setBackground("palegoldenrod")

        # Winner
        message = Text(Point(150, 50), f"\U0001F451 Winner {winner} \U0001F451")
        message.setSize(20)
        message.setFace("courier")
        message.draw(self.window)

        # Display points
        points_text = Text(
            Point(150, 80),
            f"Player 1: {points['Player 1']}  Player 2: {points['Player 2']}",
        )
        points_text.setSize(14)
        points_text.setFace("courier")
        points_text.draw(self.window)

        # Create Play Again button
        play_again_button = Rectangle(Point(70, 115), Point(150, 155))
        play_again_button.setFill("chartreuse2")
        play_again_text = Text(Point(110, 135), "Play Again")
        play_again_text.setFace("courier")
        play_again_text.setSize(12)
        play_again_button.draw(self.window)
        play_again_text.draw(self.window)

        # Create Quit button
        quit_button = Rectangle(Point(160, 115), Point(240, 155))
        quit_button.setFill("orangered1")
        quit_text = Text(Point(200, 135), "Quit")
        quit_text.setFace("courier")
        quit_text.setSize(12)
        quit_button.draw(self.window)
        quit_text.draw(self.window)

    def get_choice(self):
        """
        Purpose: Get the user's choice (Play Again or Quit) based on mouse clicks in the score window.
        Parameters: There is self which is used to access variables in the class.
        Return: Str. Either "play_again" or "quit" depending on what the user clicks.
        """
        while True:
            click_point = self.window.checkMouse()
            if click_point is not None:
                x, y = int(click_point.getX()), int(click_point.getY())
                if 70 <= x <= 150 and 115 <= y <= 155:
                    return "play_again"
                elif 160 <= x <= 240 and 115 <= y <= 155:
                    return "quit"


def main():
    """
    Purpose: This is the main function to start the game. Sets the window name, the background, creates the board from the class Board. Sets the colour of the players and their locations from the Player class. Creates a section below the game board where the quit and reset buttons are and status and coordinates are. There is a game loop which shows that status of which players turn it is and it switches when the players turn is over. Makes the quit and reset buttons work. Sees and displays where the user clicked on the game and tells the coordinates or if it is not valid, it displays that it is not valid. The whole game logic.
    Parameters: None.
    Return: None.
    """
    splash_screen = SplashScreen()
    choice = splash_screen.get_choice()
    splash_screen.window.close()

    if choice == "quit":
        return

    points = {"Player 1": 0, "Player 2": 0}  # Initialize points

    while True:
        window = GraphWin(
            "Kamil Malkowski - Icebreaker Game Version 3.0 - 12/08/23", 400, 500
        )
        window.setBackground("lightgrey")
        board = Board(window)

        player2 = Player(window, "red", 0, 0)
        player1 = Player(window, "blue", 7, 7)

        board.current_action = "move"

        status_text = Text(Point(65, 430), f"PLAYER {board.turn + 1}:")
        status_text.setFace("courier")
        status_text.draw(window)

        coordinates_text_player = Text(Point(125, 430), f"{player2.location}")
        coordinates_text_player.setFace("courier")
        coordinates_text_player.draw(window)

        instruction_text = Text(Point(100, 445), "Move")
        instruction_text.setFace("courier")
        instruction_text.draw(window)

        current_display = Text(Point(100, 460), "")
        current_display.setFace("courier")
        current_display.draw(window)

        winner_display = Text(Point(100, 475), "")
        winner_display.setFace("courier")
        winner_display.draw(window)

        quit_button = Rectangle(Point(250, 415), Point(350, 445))
        quit_button.setFill("orangered1")
        quit_text = Text(Point(300, 430), "Quit")
        quit_text.setFace("courier")
        quit_button.draw(window)
        quit_text.draw(window)

        reset_button = Rectangle(Point(250, 455), Point(350, 485))
        reset_button.setFill("gold2")
        reset_text = Text(Point(300, 470), "Reset")
        reset_text.setFace("courier")
        reset_button.draw(window)
        reset_text.draw(window)

        while True:
            status_text.setText(f"PLAYER {board.turn + 1}:")
            click_point = window.checkMouse()
            if click_point is not None:
                x, y = int(click_point.getX()), int(click_point.getY())
                # Quit button
                if 250 <= x <= 350 and 415 <= y <= 445:
                    current_display.setText("bye")
                    window.getMouse()
                    window.close()
                    return
                # Reset button
                elif 250 <= x <= 350 and 455 <= y <= 485:
                    current_display.setText("reset")
                    board.reset(player1, player2)
                    coordinates_text_player.setText(f"{player2.location}")
                else:
                    x, y = x // 50, y // 50
                    current_display.setText(f"Mouse: ({x}, {y})")

                    if board.on_map(x, y) and board.isIce(x, y):
                        if board.turn == 1:
                            # For player 1
                            if board.current_action == "move" and board.is_valid_move(
                                player1, x, y, player1, player2
                            ):
                                board.movePlayer(player1, x, y)
                                coordinates_text_player.setText(f"{player1.location}")
                                board.current_action = (
                                    "break"  # Set the action to break after moving
                                )
                                instruction_text.setText("Break Ice")
                            elif board.current_action == "break" and board.breakIce(
                                x, y, player1, player2
                            ):
                                instruction_text.setText("Move")
                            else:
                                current_display.setText("not valid")
                        else:
                            # For player 2
                            if board.current_action == "move" and board.is_valid_move(
                                player2, x, y, player1, player2
                            ):
                                board.movePlayer(player2, x, y)
                                coordinates_text_player.setText(f"{player2.location}")
                                board.current_action = (
                                    "break"  # Set the action to break after moving
                                )
                                instruction_text.setText("Break Ice")
                            elif board.current_action == "break" and board.breakIce(
                                x, y, player1, player2
                            ):
                                instruction_text.setText("Move")
                            else:
                                current_display.setText("not valid")
                    else:
                        current_display.setText("not valid")

                # Detect and display winner
                game_over, winner = board.detect_winner(player1, player2)
                if game_over:
                    winner_display.setText(f"Winner: {winner}")
                    points[winner] += 1  # Update points for the winner
                    score_screen = ScoreScreen(winner, points)
                    choice = score_screen.get_choice()
                    score_screen.window.close()

                    if choice == "quit":
                        window.close()
                        return
                    elif choice == "play_again":
                        window.close()
                        break


if __name__ == "__main__":
    main()
