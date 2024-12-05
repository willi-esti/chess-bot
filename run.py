from selenium import webdriver
from stockfish import Stockfish

from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

import clipboard, time, pyautogui, random, keyboard, sys, winsound
import msvcrt as m

from dotenv import load_dotenv
import os



def log(message):
    print(message)
    escaped_message = message.replace("'", "\\'").replace("\n", "\\n")
    browser.execute_script(f"console.log('{escaped_message}');")

def connect():
	browser.get('https://www.chess.com/login_and_go')
	browser.execute_script(debug)

	login_input=False
	login_input = browser.find_element("id", "username")

	while login_input == False :
		try:
			login_input = browser.find_element("id", "username")
		except:
			log("Loading page ...")

		time.sleep(1)

	#login_input = browser.find_element("id", "login")
	login_input.send_keys("test@gmail.com")

	pwd_input = browser.find_element("id", "password")
	pwd_input.send_keys("test")

	search_button = browser.find_element("id", "login")
	search_button.click()

	#browser.execute_script("document.getElementsByClassName('ui_outside-close-component')[0].click()")

	browser.get('https://www.chess.com/play/online')
	browser.execute_script(debug)

	calibrate()





def new_game():
	time.sleep(5)
	if browser.execute_script("if (document.getElementsByClassName('notification-toaster-link').length >= 2) {document.getElementsByClassName('notification-toaster-link')[1].click(); return 1}") != 1:
		browser.get('https://www.chess.com/play/online')
		browser.execute_script(debug)

		print(1)
		browser.execute_script("document.getElementsByClassName('selector-button-button')[0].click()")
		print(2)
		time.sleep(1)


		browser.execute_script(find_and_click + "find_and_click('button', '1 min')")

		print(3)
		time.sleep(1)

		browser.execute_script(find_and_click + "find_and_click('button', 'Play')")

		print(4)
		time.sleep(1)



def new_game_guest():
	browser.get('https://www.chess.com/play/online')
	browser.execute_script(debug)
	#browser.get('https://www.chess.com/game/live/41221211291')


	time.sleep(1)
	if is_first_browser_load == 0:
		log("Accepting cookies ... (Skip)")
		time.sleep(5)
		browser.execute_script("document.getElementById('onetrust-accept-btn-handler').click();")
		

		time.sleep(2)

		#for i in range(10000):
			#if keyboard.is_pressed('q'):
			#	print('Pause')
			#	winsound.Beep(2500, 200)
			#	return 1
			#	input()
		#	time.sleep(0.1)

		log("Clicking on the time button ...")
		browser.execute_script("document.getElementsByClassName('selector-button-button')[0].click()")
		
		time.sleep(1)

		log("Selecting 10 min ...")
		browser.execute_script(find_and_click + "find_and_click('button', '10 min')")

		time.sleep(1)

		log("Clicking on the play button ...")
		browser.execute_script(find_and_click + "find_and_click('button', 'Jouer', 'Play')")


		time.sleep(1)

		log("Clicking on the play as a guest button ...")
		browser.execute_script("document.getElementById('guest-button').click()")

		log("Setting up the board ...")
		browser.execute_script("document.getElementById('board-controls-settings').click();")
		time.sleep(2)
		browser.execute_script("document.getElementsByClassName('tabs-tab')[4].click();")
		time.sleep(1)
		browser.execute_script(find_and_click + "find_and_click('button', 'En direct');")
		time.sleep(1)
		browser.execute_script("document.getElementById('gameplay.live.auto_promote_queen').click();")
		time.sleep(1)
		browser.execute_script(find_and_click + "find_and_click('button', 'Sauvegarder')")
		time.sleep(1)




def new_game_manual(who_move):


	while browser.current_url.find('live') == -1:
		print(".", end="")
		time.sleep(0.1)
	#print('live')


	print("22222222")

	while browser.execute_script("if (document.getElementsByClassName('ui_v5-button-component ui_v5-button-primary ui_v5-button-large ui_v5-button-full').length > 0) if (document.getElementsByClassName('ui_v5-button-component ui_v5-button-primary ui_v5-button-large ui_v5-button-full')[0].innerText == 'PLAY' || document.getElementsByClassName('ui_v5-button-component ui_v5-button-primary ui_v5-button-large ui_v5-button-full')[0].innerText == 'JOUER') return 1") != 1:
		print(".", end="")
		time.sleep(0.1)
	#print('play')

	print("33333333")
	time.sleep(1)


def calibrate():
	log("\nCalibrating ...")
	global white_rook, black_rook
	white_rook = browser.execute_script(get_element_position + "return getElementPosition(document.getElementsByClassName('square-11')[0]);")
	log("\nWhite rook position : " + str(white_rook))
	black_rook = browser.execute_script(get_element_position + "return getElementPosition(document.getElementsByClassName('square-88')[0]);")
	log("\nBlack rook position : " + str(black_rook))
	winsound.Beep(2500, 200)


#print(white_rook, black_rook)
# w Point(x=373, y=232) Point(x=1420, y=341)
# b Point(x=410, y=1344) Point(x=1420, y=341)

def check_castle(castle, castlew, castleb):
	if (browser.execute_script("if (document.getElementsByClassName('wk')[0].classList[2] == 'square-51') return 1")) != 1:
		castlew = False
	if (browser.execute_script("if (document.getElementsByClassName('bk')[0].classList[2] == 'square-58') return 1")) != 1:
		castleb = False

	if castlew == False and castleb == False:
		castle = ' -'
	elif castlew == False and castleb == True:
		castle = ' KQ'
	elif castlew == True and castleb == False:
		castle = ' kq'

	return castle, castlew, castleb


def move_mouse(stockfish_best_move, a1, h8, space_between_squares):
	log("\nMoving mouse ...")
	log("\nGetting position ...")
	browser.execute_script("game.move('" + stockfish_best_move + "')")
	

def highlight_move(stockfish_best_move, fenjs):
	log("\nHighlighting move ...")
	highlight = highligh_js + "removeColorBestMove();colorBestMove(\"" + stockfish_best_move + "\")"
	browser.execute_script(highlight)
	while fenjs == browser.execute_script(fen_js):
		time.sleep(0.5)

def wait():
    m.getch()


#connect()

# Load environment variables from .env file
load_dotenv()

# Get variables
edge_driver_path = os.getenv("EDGE_DRIVER_PATH")
stockfish_path = os.getenv("STOCKFISH_PATH")

# Set up the Edge options (optional)
edge_options = Options()
edge_options.add_argument("--start-maximized")  # Start browser maximized
# open f12
edge_options.add_argument("--auto-open-devtools-for-tabs")  # Open DevTools

# Set up the WebDriver service
service = Service(executable_path=edge_driver_path)

# Create the WebDriver instance
browser = webdriver.Edge(service=service, options=edge_options)
#browser.maximize_window()

stockfish = Stockfish(path=stockfish_path)
#stockfish.set_skill_level(1)
#stockfish.set_elo_rating(500)
#stockfish.set_depth(3)
#log("Stockfish parameters:\n")
#log(stockfish.get_parameters())

who_move  = ' w'
who_turn = who_move
castle = ' KQkq'
castlew = True
castleb = True
move_count = 0
white_rook = None
black_rook = None
js = None

log("\nDefining JS functions ...")

debug = """
// Create a div to display the mouse position
const positionDiv = document.createElement('div');
positionDiv.style.position = 'fixed';
positionDiv.style.top = '0';
positionDiv.style.left = '0';
positionDiv.style.backgroundColor = 'rgba(0, 0, 0, 0.7)';
positionDiv.style.color = 'white';
positionDiv.style.padding = '5px 10px';
positionDiv.style.zIndex = '1000';
positionDiv.style.fontFamily = 'Arial, sans-serif';
positionDiv.style.fontSize = '14px';
document.body.appendChild(positionDiv);

// Update the div with the mouse position
document.addEventListener('mousemove', (event) => {
    positionDiv.textContent = `Mouse X: ${event.pageX}, Mouse Y: ${event.pageY}`;
});
"""

create_squares = """
function create_piece(square_num)
{
    // Select the target container by ID
    const boardSingle = document.getKElementsByClassName('board')[0];
    
    // Check if the container exists
    if (boardSingle) {
        // Create a new div element
        const pieceDiv = document.createElement('div');

        // Add the desired classes to the new div
        pieceDiv.className = 'piece square-' + square_num;

        // Add inline styles (if any)
        pieceDiv.style.cssText = ''; // No styles provided, this is an empty style

        // Append the new div to the target container
        boardSingle.appendChild(pieceDiv);

        console.log('Piece created and added to #board-single:', pieceDiv);
    } else {
        console.error('Element with ID "board-single" not found.');
    }

}


create_piece('84')
for (let i = 1; i <= 8; i++) {
    for (let j = 1; j <= 8; j++) {
        create_piece(i + '' + j)
    }
}
"""


get_element_position = """
function getElementPosition(element) {
    if (element) {
        const rect = element.getBoundingClientRect();
        console.log('X:', rect.x);
        console.log('Y:', rect.y);
		console.log('Bottom:', rect.bottom);
		console.log('Right:', rect.right);
        return { x: rect.x, y: rect.y };
    } else {
        console.log('Element not found');
		return null;
    }
}
// Usage example:
// getElementPosition(document.getElementsByClassName('square-18')[0]);
"""

highligh_js= """
function getSquareFrom(e) {
    return x = e.split("")[0], y = e.split("")[1], "a" == x ? x = 10 : "b" == x ? x = 20 : "c" == x ? x = 30 : "d" == x ? x = 40 : "e" == x ? x = 50 : "f" == x ? x = 60 : "g" == x ? x = 70 : "h" == x && (x = 80), parseInt(x) + parseInt(y)
}

function getSquareTo(e) {
    return x = e.split("")[2], y = e.split("")[3], "a" == x ? x = 10 : "b" == x ? x = 20 : "c" == x ? x = 30 : "d" == x ? x = 40 : "e" == x ? x = 50 : "f" == x ? x = 60 : "g" == x ? x = 70 : "h" == x && (x = 80), parseInt(x) + parseInt(y)
}

function colorBestMove(e) {
    var t = document.createElement("div");
    t.id = "color_square", t.className = "highlight square-" + getSquareFrom(e), t.style = "background-color: rgb(0, 255, 255); opacity: 0.2", document.getElementsByClassName("board")[0].appendChild(t);
    var o = document.createElement("div");
    o.id = "color_square1", o.className = "highlight square-" + getSquareTo(e), o.style = "background-color: rgb(0, 255, 255); opacity: 0.2", document.getElementsByClassName("board")[0].appendChild(o)
}

function removeColorBestMove() {
    a = document.getElementById("color_square"), b = document.getElementById("color_square1"), null != a && a.remove(), null != b && b.remove()
}
"""

fen_js = """
if (typeof game !== 'undefined' && game !== null) {
    game.getFEN()
}
"""

find_and_click = """
function find_and_click(tag_name, text, text2="text")
{
	playButton = ""
	while(playButton == "")
	{
		for (i = 0; i < document.getElementsByTagName(tag_name).length; i++) { 
			if (document.getElementsByTagName(tag_name)[i].innerText == text || document.getElementsByTagName(tag_name)[i].innerText == text2)
			{
				playButton = "1"
				document.getElementsByTagName(tag_name)[i].click()
			}
		}
	}
}
"""

whos_turn = """
if (document.getElementsByClassName('clock-player-turn')[0])
{
	clock = document.getElementsByClassName('clock-player-turn')[0]
	if (clock.parentElement.parentElement.id == 'board-layout-player-bottom')
	{
		return ' w';
	}
	else
	{
		return ' b';
	}	
}
"""

log("\nRunning debug script ...")
is_first_browser_load = False

while True:
	#new_game()
	log("\nStarting new game ...")
	new_game_guest()
	log("\nNew game started ...")
	if is_first_browser_load == 0:
		is_first_browser_load = 1
	calibrate()

	move_count = 0

	log("\nResetting variables fen and flipped ...")
	old_fen=None
	flipped = 0

	while browser.execute_script("return document.getElementsByClassName('game-over-modal-content').length") != 1:
		#print ("Current position: " + str(mouse.position))
		if browser.execute_script("if (document.getElementsByClassName('clock-player-turn')[0]) return 1") == 1:
			if keyboard.is_pressed('q'):
				log("Game paused ...")
				input()

			if (flipped == 0):
				who_move  = ' w'
				if browser.execute_script("return document.getElementsByClassName('flipped').length") == 1:
					log("Flipping board ...")
					time.sleep(5)
					browser.execute_script("return document.getElementById('board-controls-flip').click()")
					who_move  = ' b'
				flipped = 1

			who_turn = browser.execute_script(whos_turn)
			if who_move == who_turn:
				log("\nMy turn ...")
				move_count += 1
				print(fen_js)
				fenjs = browser.execute_script(fen_js)

				#castle, castlew, castleb = check_castle(castle, castlew, castleb)

				fen = fenjs
				# TypeError: can only concatenate str (not "NoneType") to str
				log("\nFEN: " + str(fen))
				#log("\nFEN: " + fen)
				
				# To prevent crashing the browser when stockfish crashes
				try:
					stockfish.set_fen_position(fen)
					stockfish_best_move = stockfish.get_best_move()
				except:
					log("\nStockfish crashed ...")
					#break
				
				log("\nStockfish best move: " + stockfish_best_move)

				if stockfish_best_move == None:
					break

				move_mouse(stockfish_best_move)
				highlight_move(stockfish_best_move, fenjs)

				#mouse.move(0,0)
				clipboard.copy("")
				fen = fenjs

				old_fen = fen
				print(".", end="")

			time.sleep(0.1)
			who_turn = None

"""

function getSquareFrom(bestmove)
{
    x = bestmove.split("")[0];
    y = bestmove.split("")[1];

    if (x == "a") x = 10;
    else if (x== "b") x = 20;
    else if (x== "c") x = 30;
    else if (x== "d") x = 40;
    else if (x== "e") x = 50;
    else if (x== "f") x = 60;
    else if (x== "g") x = 70;
    else if (x== "h") x = 80;
    return parseInt(x)+parseInt(y)
}

function getSquareTo(bestmove)
{
    x = bestmove.split("")[2];
    y = bestmove.split("")[3];

    if (x == "a") x = 10;
    else if (x== "b") x = 20;
    else if (x== "c") x = 30;
    else if (x== "d") x = 40;
    else if (x== "e") x = 50;
    else if (x== "f") x = 60;
    else if (x== "g") x = 70;
    else if (x== "h") x = 80;
    return parseInt(x)+parseInt(y)
}


function colorBestMove(bestmove)
{

    var color_square = document.createElement("div");
    color_square.id = "color_square";
    color_square.className = "highlight square-"+getSquareFrom(bestmove);
    color_square.style="background-color: rgb(0, 255, 255); opacity: 0.2";


    document.getElementsByClassName('board')[0].appendChild(color_square);

    
    var color_square1 = document.createElement("div");
    color_square1.id = "color_square1";
    color_square1.className = "highlight square-"+getSquareTo(bestmove);
    color_square1.style="background-color: rgb(0, 255, 255); opacity: 0.2";


    document.getElementsByClassName('board')[0].appendChild(color_square1);
    
}


function removeColorBestMove()
{
	a = document.getElementById('color_square')
	b = document.getElementById('color_square1')
	if (a != null) a.remove();
	if (b != null) b.remove();   
}

"""