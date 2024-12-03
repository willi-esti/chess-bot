# Chess Bot

This project is a chess bot that plays chess on [chess.com](https://www.chess.com) using Selenium WebDriver and Stockfish chess engine. The bot automates the process of playing chess games, including logging in, starting new games, and making moves based on Stockfish's recommendations.

## Prerequisites

- Python 3.x
- Selenium
- Stockfish
- PyAutoGUI
- Keyboard
- Winsound
- Clipboard

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/willi-esti/chess-bot
    cd chess-bot
    ```

2. Install the required Python packages:
    ```sh
    pip install selenium pyautogui keyboard clipboard python-dotenv
    ```

3. Download the Edge WebDriver and place it in the `selenium_driver` directory:
    - [Download Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

4. Download Stockfish and place it in the `stockfish` directory:
    - [Download Stockfish](https://stockfishchess.org/download/)

## Usage

1. Update the `connect` function in `mouse_moves.py` with your chess.com login credentials.

2. Run the script:
    ```sh
    python mouse_moves.py
    ```

## Script Overview

- `connect()`: Logs into chess.com and navigates to the online play page.
- `new_game()`: Starts a new game.
- `new_game_guest()`: Starts a new game as a guest.
- `new_game_manual(who_move)`: Manually starts a new game.
- `calibrate()`: Calibrates the bot by locating specific images on the screen.
- `check_castle(castle, castlew, castleb)`: Checks the castling status.
- `move_mouse(bm, a1, h8, x_space, y_space)`: Moves the mouse to make a move.
- `highlight_move(bm, fenjs)`: Highlights the best move on the board.
- `wait()`: Waits for a key press.

## Notes

- Ensure that the calibration images (`wr.png` and `br.png`) are placed in the `calibration_images` directory.
- The script uses the Stockfish chess engine to determine the best moves.
- The script interacts with the chess.com website using Selenium WebDriver.

## License

This project is licensed under the MIT License.