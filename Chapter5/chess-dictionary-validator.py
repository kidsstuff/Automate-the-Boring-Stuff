def isValidChessboard(board):
    wPieces = bPieces = 0
    wSet = {"king": 0, "queen": 0, "rook": 0, "bishop": 0, "knight": 0, "pawn": 0}
    bSet = {"king": 0, "queen": 0, "rook": 0, "bishop": 0, "knight": 0, "pawn": 0}
    goodSet = {"king": 1, "queen": 1, "rook": 2, "bishop": 2, "knight": 2, "pawn": 8}
    for key, piece in board.items():
        try:
            # Check valid space from 1a to 8h
            if (1 < int(key[0]) > 8) or (not(key[1] in "abcdefgh")) or (len(key) != 2):
                print(f"Unvalid postion: {key}")
                return False
            # Check piece names begin with either w or b
            if piece[0] == 'w' :
                wPieces += 1
                wSet[piece[1:]] += 1
            elif piece[0] == 'b':
                bPieces += 1
                bSet[piece[1:]] += 1
            else:
                print(f"Piece name doesn't begin with a w or b: {piece}")
                return False

            # Each set consists of 16 pieces: 
            if wPieces > 16 or bPieces > 16:
                print("One set has more than 16 pieces.")
                return False
            # Check one king, one queen, two rooks, two bishops, two knights, and eight pawns
            for check, number in goodSet.items():
                if checkPiece(wSet, check, number):
                    print(f"Two many white {check}s.")
                    return False
                if checkPiece(bSet, check, number):
                    print(f"Two many black {check}s.")
                    return False

        except Exception:
            print("Excepton error")
            return False
    return True

# Check max number of chess piece
def checkPiece(pieces, piece, maxNumber):
    return pieces[piece] > maxNumber

# Tests
board1={'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '3a': 'wpawn'}
board2={'1h': 'bking', '6c': 'queen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '3a': 'pawn'}
board3={'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '3a': 'wpawn', '3c': 'wking'}
board4={'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '3a': 'wpawn', '3c': 'wpawn', '9z': 'wpawn'}
board5={'1h': 'bking', '6c': 'wqueln', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '3a': 'wpawn'}
print("board1:" + str(isValidChessboard(board1)))
print("board2:" + str(isValidChessboard(board2)))
print("board3:" + str(isValidChessboard(board3)))
print("board4:" + str(isValidChessboard(board4)))
print("board5:" + str(isValidChessboard(board5)))
