# Generate-and-Fix-ChessBoard
This python program generates a chessboard with several errors (unless you are lucky), and then attempts to fix it.

GenerateAndFixChessBoard.py is the main file that is to be run. This file will generate a chessboard with pieces, then check if every piece is valid and in a valid spot on the board. Pieces that trigger an error in some way will be regenerated. This may not fix the problem which will attempted to be fixed again during the next round. At each stage the full error list is printed by pprint.

Eventually, I may add visualization or the ability to play the position via some open source chess engine like Stockfish.
