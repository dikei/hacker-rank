def next_move(posx, posy, board):
    def get_dirts():
        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if col == 'd':
                    yield i, j

    def calculate_path(botx, boty, dirtx, dirty):
        if botx > dirtx:
            verticalMove = ['UP' for _ in range(0, botx - dirtx)]
        else:
            verticalMove = ['DOWN' for _ in range(0, dirtx - botx)]

        if boty > dirty:
            horizontalMove = ['LEFT' for _ in range(0, boty - dirty)]
        else:
            horizontalMove = ['RIGHT' for _ in range(0, dirty - boty)]

        move = verticalMove + horizontalMove
        weight = len(move)
        if weight:
            return move[0], weight
        else:
            return '', None

    if board[posx][posy] == 'd':
        print "CLEAN"
        return

    min_weight = 1000
    next_move = None
    for dirtx, dirty in get_dirts():
        move, weight = calculate_path(posx, posy, dirtx, dirty)
        if weight is not None and weight < min_weight:
            min_weight = weight
            next_move = move

    if next_move is not None:
        print next_move