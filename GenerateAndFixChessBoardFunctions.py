# a collection of functions for the Generate and Fix Chess Board
import pprint
import random


def generateChessBoard():
    # this will create a 32 length dictionary with the first term being a random alg notation, and piece
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    ints = list(range(1, 12))
    colors = ['b', 'w', 'r', 'g']
    pieces = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king', 'jester', 'wizard', 'archer', 'pawn', 'pawn', 'pawn']
    Board = {}

    while len(Board) < 32:
        # generating alg notation
        algNotation = str(random.choice(letters)) + '|' + str(random.choice(ints))

        # generating piece
        piece = random.choice(colors) + random.choice(pieces)

        try:
            Board.update({algNotation: piece})
        except KeyError:
            continue
    return Board


def initErrorList(chessBoard):
    # create the first list of errors
    lengthErrorList, invalidIntList, invalidLetterList, pieceColorErrorList, pieceNameErrorList, = {}, {}, {}, {}, {},
    errorList = {'length': lengthErrorList, 'invalidInt': invalidIntList, 'invalidLetter': invalidLetterList,
                 'pieceColor': pieceColorErrorList, 'pieceName': pieceNameErrorList}
    chessPieces = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']

    for i, j in chessBoard.items():
        item = {i: j} # Making a dict to keep track of the specific thing
        findDiv = i.find('|')

        if len(i) != 3:
            lengthErrorList.update(item)

        try:
            if int(i[findDiv + 1:]) not in range(1, 9):
                invalidIntList.update(item)
        except ValueError:
            invalidIntList.update(item)

        if i[0] < 'a' or i[0] > 'h':
            invalidLetterList.update(item)

        if j[0] not in ['b', 'w']:
            pieceColorErrorList.update(item)

        if j[1:] not in chessPieces:
            pieceNameErrorList.update(item)

    return chessBoard, errorList


def validateErrorList(errorList):
    # this will basically try to see if fixChessBoard successfully fixed errors by checking the errorList to see if they
    # are still in error

    for error, pairs in errorList.items():
        for i, j in list(pairs.items()):
            findDiv = i.find('|')
            piecePairs = {}
            piecePairs.update({i: j})

            if error == 'length':
                if len(i) == 3:
                    pairs.pop(i)

            elif error == 'invalidInt':
                try:
                    if int(i[findDiv + 1:]) in range(1, 9):
                        pairs.pop(i)
                except ValueError:
                    continue

            elif error == 'invalidLetter':
                if i[:findDiv] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
                    pairs.pop(i)

            elif error == 'pieceColor':
                if j[0] in ['b', 'w']:
                    pairs.pop(i)

            elif error == 'pieceName':
                if j[1:] in ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']:
                    pairs.pop(i)

    return errorList


def fixChessBoard(chessBoard, errorList):
    # this is meant to take a look at the errors and try to reroll certain aspects of the dict set.
    # It will then update the chessboard and error list.
    # This is for the most part just a way to activate the various fix functions

    for error, errorPairs in errorList.items():
        if len(errorPairs) == 0:
            continue
        else:
            for i, j in list(errorPairs.items()):
                piecePairs = {}
                piecePairs.update({i: j})

                if error == 'length':
                    errorList, chessBoard = fixLenError(piecePairs, errorList, chessBoard)

                elif error == 'invalidInt':
                    errorList, chessBoard = fixInvalidInt(piecePairs, errorList, chessBoard)

                elif error == 'invalidLetter':
                    errorList, chessBoard = fixInvalidLetter(piecePairs, errorList, chessBoard)

                elif error == 'pieceColor':
                    errorList, chessBoard = fixPieceColor(piecePairs, errorList, chessBoard)

                elif error == 'pieceName':
                    errorList, chessBoard = fixPieceName(piecePairs, errorList, chessBoard)

    return chessBoard, errorList


def fixLenError(pieceDict, errorList, chessBoard):
    # Attempts to fix the algebraic notation by checking if either half is too long, and rerolling it,
    # then checking if that ALg Notation exists and if it does it re-rolls again

    pieceTuple = list(pieceDict.items())[0]  # Dict_items obj into a list, indexed for the tuple within
    findDiv = pieceTuple[0].find('|')

    while True:

        if len(pieceTuple[0][:findDiv]) > 1:
            newLetter = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'])
        else:
            newLetter = pieceTuple[0][:findDiv]

        if len(pieceTuple[0][findDiv + 1:]) > 1:
            newInt = str(random.choice(list(range(1, 12))))
        else:
            newInt = pieceTuple[0][findDiv + 1:]

        newAlgNot = newLetter + '|' + newInt
        newPair = {newAlgNot: pieceTuple[1]}

        if newAlgNot not in [i for i in chessBoard.keys()]:
            break
        else:
            continue

    errorList, chessBoard = updateErrorsBoard(newPair, errorList, pieceTuple, chessBoard)

    return errorList, chessBoard


def fixInvalidInt(pieceDict, errorList, chessBoard):
    # Attempts to fix an invalid integer in the first half of the Algebraic Notation

    pieceTuple = list(pieceDict.items())[0]  # Dict_items obj into a list, indexed for the tuple within
    findDiv = pieceTuple[0].find('|')

    while True:
        if pieceTuple[0][findDiv + 1:] not in list(range(1, 9)):
            newInt = str(random.choice(list(range(1, 12))))
        else:
            newInt = pieceTuple[0][findDiv + 1:]

        newAlgNot = pieceTuple[0][:findDiv] + '|' + newInt
        newPair = {newAlgNot: pieceTuple[1]}
        keys = [i for i in chessBoard.keys()]

        if newAlgNot not in keys:
            print(f'{newAlgNot} is not in the Board.')
            break

    errorList, chessBoard = updateErrorsBoard(newPair, errorList, pieceTuple, chessBoard)

    return errorList, chessBoard


def fixInvalidLetter(pieceDict, errorList, chessBoard):
    # Attempts to fix an invalid letter in the second half of the Algebraic Notation

    pieceTuple = list(pieceDict.items())[0]  # Dict_items obj into a list, indexed for the tuple within
    findDiv = pieceTuple[0].find('|')
    while True:
        if pieceTuple[0][:findDiv] not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
            newLetter = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'])
        else:
            newLetter = pieceTuple[0][:findDiv]

        newAlgNot = newLetter + '|' + pieceTuple[0][findDiv + 1:]
        newPair = {newAlgNot: pieceTuple[1]}

        if newAlgNot not in [i for i in chessBoard.keys()]:
            break
        else:
            continue

    errorList, chessBoard = updateErrorsBoard(newPair, errorList, pieceTuple, chessBoard)

    return errorList, chessBoard


def fixPieceColor(pieceDict, errorList, chessBoard):
    # Attempts to fix the color of a piece by re-rolling the first letter of the value of a piece dictionary

    pieceTuple = list(pieceDict.items())[0]  # Dict_items obj into a list, indexed for the tuple within

    if pieceTuple[1][0] not in ['w', 'b']:
        newColor = random.choice(['b', 'w', 'r', 'g'])
    else:
        newColor = pieceTuple[1][0]

    newPieceCombo = newColor + pieceTuple[1][1:]
    newPair = {pieceTuple[0]: newPieceCombo}

    errorList, chessBoard = updateErrorsBoard(newPair, errorList, pieceTuple, chessBoard)

    return errorList, chessBoard


def fixPieceName(pieceDict, errorList, chessBoard):
    # Attempts to fix the piece name of a piece by re-rolling everything past the first letter of the value of a
    # piece dictionary

    pieceTuple = list(pieceDict.items())[0]  # Dict_items obj into a list, indexed for the tuple within

    if pieceTuple[1][1:] not in ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']:
        newName = random.choice(
            ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king', 'jester', 'wizard', 'archer', 'pawn', 'pawn', 'pawn'])
    else:
        newName = pieceTuple[1][1:]

    newPieceCombo = pieceTuple[1][0] + newName
    newPair = {pieceTuple[0]: newPieceCombo}

    errorList, chessBoard = updateErrorsBoard(newPair, errorList, pieceTuple, chessBoard)

    return errorList, chessBoard


def updateErrorsBoard(newPair, errorList, pieceTuple, chessBoard):
    # Will update both the chesBoard and errorList to reflect the new pair generated.
    # First, the Chessboard will be done, which is relatively simple (remove old based on pieceTuple,
    # add new based on newPair)

    dictKey = pieceTuple[0]
    chessBoard.pop(dictKey)
    chessBoard.update(newPair)

    # Now for the more complex process of update the errorList, which is not too bad either.

    for error in errorList.items():
        if error[1].get(dictKey) is None:
            continue
        else:
            error[1].pop(dictKey)
            error[1].update(newPair)

    return errorList, chessBoard
