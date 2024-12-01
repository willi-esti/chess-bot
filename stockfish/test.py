

from stockfish import Stockfish

stockfish = Stockfish(path="stockfish/stockfish_14.1_win_x64_avx2.exe")


#fen = "position fen r4r1k/1ppq3p/p2p1pp1/8/2B1PpR1/2PP1Q2/P1P2P1P/2K5 b KQkq - - 20"
#r1b4r/2ppkp1p/5p2/p7/p3PN2/5P2/1P2RbPP/7K b KQkq - - 23
#fen = "r1b4r/2ppkp1p/5p2/p7/p2bPN2/5P2/1P4PP/4R2K b KQkq - - 22"
#fen = "r3k2r/3R4/8/5p2/1p3q1p/4p3/2P1Q1P1/7K b - - - 35"




# Real bad
# position fen 4rk1Q/4q3/p2p1p1p/6p1/3B1bP1/P1P2N1P/1P3PK1/3R4 w - - - 35
#fen = "4rk1Q/4q3/p2p1p1p/6p1/3B1bP1/P1P2N1P/1P3PK1/3R4 w - - 0 1"
fen = "rn2k2r/pp1q1pp1/2p5/2Pp4/1P1Pp3/P3P1N1/1B1N1nBP/3R2K1 b KQ - - 19"

print("1")
stockfish.set_fen_position(fen)
print("2")
try :
	bm = stockfish.get_best_move_time(10)
except:
	print('ok')

print("3")
print(bm)

