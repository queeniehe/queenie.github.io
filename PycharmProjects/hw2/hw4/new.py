def getBoardCopy(b):
    # Make a duplicate of the board. When testing moves we don't want to change the actual board
    dupeBoard = []
    for j in b:
        dupeBoard.append(j)

    return dupeBoard
print (getBoardCopy(b))
