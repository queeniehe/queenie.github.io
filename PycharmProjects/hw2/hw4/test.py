class computer():
  """
  This is the class to be specialized by students.
  """

  def move(self, match):

   def getBoardCopy(b):
    # Make a duplicate of the board. When testing moves we don't want to
    # change the actual board
    dupeBoard = []
    for j in b:
        dupeBoard.append(j)
    return dupeBoard
   def testWinMove(b, mark, i):
    # b = the board
    # mark = 0 or X
    # i = the square to check if makes a win
    bCopy = getBoardCopy(b)
    bCopy[i] = mark
    return checkWin(bCopy, mark)
   def testForkMove(b, mark, i):
    # Determines if a move opens up a fork
    bCopy = getBoardCopy(b)
    bCopy[i] = mark
    winningMoves = 0
    for j in range(0, 9):
        if testWinMove(bCopy, mark, j) and bCopy[j] == ' ':
            winningMoves += 1
    return winningMoves >= 2
   def getComputerMove(b):
    # Check computer win moves
    for i in range(0, 9):
        if b[i] == ' ' and testWinMove(b, 'X', i):
            return i
    # Check player win moves
    for i in range(0, 9):
        if b[i] == ' ' and testWinMove(b, '0', i):
            return i
    # Check computer fork opportunities
    for i in range(0, 9):
        if b[i] == ' ' and testForkMove(b, 'X', i):
            return i
    # Check player fork opportunities, incl. two forks
    playerForks = 0
    for i in range(0, 9):
        if b[i] == ' ' and testForkMove(b, '0', i):
            playerForks += 1
            tempMove = i
    if playerForks == 1:
        return tempMove
    elif playerForks == 2:
        for j in [1, 3, 5, 7]:
            if b[j] == ' ':
                return j
    # Play center
    if b[4] == ' ':
        return 4
    # Play a corner
    for i in [0, 2, 6, 8]:
        if b[i] == ' ':
            return i
    #Play a side
    for i in [1, 3, 5, 7]:
        if b[i] == ' ':
            return i
