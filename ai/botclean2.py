def next_move(posx, posy, board):

    def get_dirts():
        tmp = []
        for i in range(posx - 1, posx + 2):
            for j in range(posy - 1, posy + 2):
                try:
                    if board[i][j] == 'd':
                        tmp.append((i, j))
                except IndexError:
                    continue
        return tmp

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
            return move, weight
        else:
            return None, None

    def getpath_to_closest(postlist):
        min_weight = 1000
        _next_move = None
        for post in postlist:
            move, weight = calculate_path(posx, posy, post[0], post[1])
            if weight is not None and weight < min_weight:
                min_weight = weight
                _next_move = move
        return _next_move, min_weight

    #Load state data
    dirt_pos = set()
    try:
        with open('board.txt', 'rb') as f:
            for row in f:
                dirt_pos.add(tuple(int(i) for i in row.split()))
    except IOError:
        pass
    dirt_pos.update(get_dirts())

    queue = []
    try:
        with open('queue.txt', 'rb') as f:
            for row in f:
                queue.append(row.strip())
    except IOError:
        pass

    bases = [(1, 1), (1, 3), (3, 3), (3, 1)]
    visited = []
    try:
        with open('visited.txt', 'rb') as f:
            for row in f:
                base = tuple((int(i) for i in row.split()))
                if base in bases:
                    bases.remove(base)
                    visited.append(base)
    except IOError:
        pass

    if (posx, posy) in bases:
        visited.append((posx, posy))
        bases.remove((posx, posy))

    if board[posx][posy] == 'd':
        dirt_pos.remove((posx, posy))
        print "CLEAN"
    else:
        if len(queue) > 0:
            print queue.pop(0)
        else:
            #Move to the closest visible dirt
            _next_move, weight = getpath_to_closest(dirt_pos)
            if _next_move is not None:
                queue.extend(_next_move)
            elif len(bases) > 0:
                _next_move, weight = getpath_to_closest(bases)
                if _next_move is not None:
                    queue.extend(_next_move)
            if len(queue) > 0:
                print queue.pop(0)

    #Save state
    with open('board.txt', 'wb') as f:
        for row in dirt_pos:
            f.write(" ".join((str(i) for i in row)) + "\n")

    with open('queue.txt', 'wb') as f:
        for item in queue:
            f.write(item + '\n')

    with open('visited.txt', 'wb') as f:
        for base in visited:
            f.write(' '.join((str(i) for i in base)) + '\n')
