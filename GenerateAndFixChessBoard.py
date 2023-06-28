# This will generate a randomized chessboard, a function will validate it. any errors will try to be fixed.
# and this will continue until the chessboard is valid.

import pprint as pp

import GenerateAndFixChessBoardFunctions as cbf

chessBoard = cbf.generateChessBoard()

chessBoard, errorList = cbf.initErrorList(chessBoard)

errors = 0
for pairs in list(errorList.values()):
    errors += len(pairs)

loopCount = 0
while errors > 0:

    chessboard, errorList = cbf.fixChessBoard(chessBoard, errorList)
    errorList = cbf.validateErrorList(errorList)

    pp.pprint(errorList)

    errors = 0
    for pairs in list(errorList.values()):
        errors += len(pairs)

    loopCount += 1
print(f'It took {loopCount} attempts to fix the chessBoard.')
pp.pprint(chessBoard)