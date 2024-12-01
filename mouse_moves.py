from selenium import webdriver
from stockfish import Stockfish

from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

import clipboard, time, pyautogui, random, keyboard, sys, winsound
import msvcrt as m



# Specify the path to the WebDriver executable
edge_driver_path = "selenium_driver/msedgedriver.exe"

# Set up the Edge options (optional)
edge_options = Options()
edge_options.add_argument("--start-maximized")  # Start browser maximized

# Set up the WebDriver service
service = Service(executable_path=edge_driver_path)

# Create the WebDriver instance
browser = webdriver.Edge(service=service, options=edge_options)



stockfish = Stockfish(path="stockfish/stockfish_14.1_win_x64_avx2.exe")
#stockfish.set_skill_level(1)
#stockfish.set_elo_rating(500)
#stockfish.set_depth(3)
#print(stockfish.get_parameters())

#browser = webdriver.Edge(executable_path="selenium_driver/msedgedriver.exe")
browser.maximize_window()

who_move  = ' w'
who_turn = who_move
castle = ' KQkq'
castlew = True
castleb = True
move_count = 0
wr = None
br = None
js = None



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
function findPiece(e) {
    piece = null, n = document.getElementsByClassName("piece").length;
    for (var o = 0; o <= n - 1; o++) name = document.getElementsByClassName("piece")[o].className.split(" ")[1], position = document.getElementsByClassName("piece")[o].className.split(" ")[2].split("-")[1], position == e && (piece = [name, position]);
    return piece
}
fen = "", count = 0;
for (var i = 8; i >= 1; i--) {
    for (var j = 1; j <= 8; j++) pos = j.toString() + i.toString(), piece = findPiece(pos), piece ? (count > 0 && (fen += count, count = 0), color = piece[0].split("")[0], p = piece[0].split("")[1], "b" == color ? fen += p.toLowerCase() : "w" == color && (fen += p.toUpperCase())) : count++;
    count > 0 && (fen += count, count = 0), fen += "/"
}
return fen
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


def connect():
	browser.get('https://www.chess.com/login_and_go')

	login_input=False
	login_input = browser.find_element("id", "username")

	while login_input == False :
		try:
			login_input = browser.find_element("id", "username")
		except:
			print("Loading page ...")

		time.sleep(1)

	#login_input = browser.find_element("id", "login")
	login_input.send_keys("test@gmail.com")

	pwd_input = browser.find_element("id", "password")
	pwd_input.send_keys("test")

	search_button = browser.find_element("id", "login")
	search_button.click()

	#browser.execute_script("document.getElementsByClassName('ui_outside-close-component')[0].click()")

	browser.get('https://www.chess.com/play/online')


	calibrate()





def new_game():
	time.sleep(5)
	if browser.execute_script("if (document.getElementsByClassName('notification-toaster-link').length >= 2) {document.getElementsByClassName('notification-toaster-link')[1].click(); return 1}") != 1:
		browser.get('https://www.chess.com/play/online')

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

	#browser.get('https://www.chess.com/game/live/41221211291')


	time.sleep(1)
	if c == 0:
		browser.execute_script(find_and_click + "find_and_click('button', 'Accepter tout')")
		calibrate()

		time.sleep(10)

		#for i in range(10000):
			#if keyboard.is_pressed('q'):
			#	print('Pause')
			#	winsound.Beep(2500, 200)
			#	return 1
			#	input()
		#	time.sleep(0.1)

		browser.execute_script("document.getElementsByClassName('selector-button-button')[0].click()")
		print(2)
		time.sleep(1)

		browser.execute_script(find_and_click + "find_and_click('button', '10 min')")

		time.sleep(1)

		browser.execute_script(find_and_click + "find_and_click('button', 'Jouer', 'Play')")


		time.sleep(1)


	if c == 0 :
		browser.execute_script(find_and_click + "find_and_click('a', 'Play as a Guest')")

	if c == 0:
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
	global wr, br

	while wr == None or br == None:
		wr = pyautogui.locateCenterOnScreen('calibration_images/wr.png', confidence=0.4)
		br = pyautogui.locateCenterOnScreen('calibration_images/br.png', confidence=0.4)
		if wr != None:
			print('Ok')
			pyautogui.moveTo(wr[0], wr[1])

		time.sleep(2)
		if br != None:
			print('Ok1')
			pyautogui.moveTo(br[0], br[1])
		time.sleep(0.5)
	winsound.Beep(2500, 200)


#print(wr, br)
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


def move_mouse(bm, a1, h8, x_space, y_space):
	x = ((ord(bm[0]) - 97)*x_space+a1[0])
	y = (a1[1]-((int(bm[1])-1)*y_space))
	x1 = ((ord(bm[2]) - 97)*x_space+a1[0])
	y1 = (a1[1]-((int(bm[3])-1)*y_space))
	#print("Pos : " + str(x) + " ,"  + str(y) + "; " + str(x1) + " ,"  + str(y1))

	if move_count < 5:
		time.sleep(random.uniform(0.1, 0.3))
	elif move_count < 15 and move_count > 5:
		time.sleep(random.uniform(0.1, 4))
	elif move_count < 20 and move_count > 15:
		time.sleep(random.uniform(0.1, 2))
	elif move_count < 25 and move_count > 20:
		time.sleep(random.uniform(0.1, 1))
	elif move_count < 40 and move_count > 25:
		time.sleep(random.uniform(0.1, 0.5))
	else:
		time.sleep(random.uniform(0.1, 0.2))

	pyautogui.moveTo(int(x), int(y))
	
	pyautogui.mouseDown();
	time.sleep(0.01)

	pyautogui.moveTo(int(x1), int(y1))

	time.sleep(0.01)
	pyautogui.mouseUp()
	

def highlight_move(bm, fenjs):
	highlight = highligh_js + "removeColorBestMove();colorBestMove(\"" + bm + "\")"
	browser.execute_script(highlight)
	while fenjs == browser.execute_script(fen_js)[:-1]:
		time.sleep(0.5)

def wait():
    m.getch()


#connect()

c = 0

while True:
	#new_game()
	new_game_guest()
	if c == 0:
		c = 1


	move_count = 0

	"""
	print("a1")
	_ = input()
	a1 = mouse.position
	print("h8")
	_ = input()
	h8 = mouse.position
	"""
	a1 = wr
	h8 = br
	#print(a1, h8)
	x_space = abs(h8[0] - a1[0])/7
	y_space = abs(a1[1] - h8[1])/7
	old_fen=None
	#game-over-modal-content

	print("lol")

	flipped = 0

	while browser.execute_script("return document.getElementsByClassName('game-over-modal-content').length") != 1:
		#print ("Current position: " + str(mouse.position))
		if browser.execute_script("if (document.getElementsByClassName('clock-player-turn')[0]) return 1") == 1:
			if keyboard.is_pressed('q'):
				print('Pause')
				input()

			if (flipped == 0):
				who_move  = ' w'
				if browser.execute_script("return document.getElementsByClassName('flipped').length") == 1:
					browser.execute_script("return document.getElementById('board-controls-flip').click()")
					who_move  = ' b'
				flipped = 1



			who_turn = browser.execute_script(whos_turn)
			if who_move == who_turn:
				move_count += 1

				fenjs = browser.execute_script(fen_js)[:-1]

				castle, castlew, castleb = check_castle(castle, castlew, castleb)

				fen = fenjs + who_move + castle + " -" + " - " + str(move_count)

				print("\n", fen, end="")


				stockfish.set_fen_position(fen)
				bm = stockfish.get_best_move()
				print(bm)

				if bm == None:
					break

				move_mouse(bm, a1, h8, x_space, y_space)
				highlight_move(bm, fenjs)

				#mouse.move(0,0)
				clipboard.copy("")
				fen = fenjs + who_move + castle + " -" + " - " + str(move_count)

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