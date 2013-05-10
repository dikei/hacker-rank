def nextMove(n, x, y, grid):
    def get_princess():
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col == 'p':
                    return i, j
        return None

    princess = get_princess()
    if not princess:
        return ""

    bot = (x, y)

    if bot[0] > princess[0]:
        verticalMove = ['UP' for _ in range(0, bot[0] - princess[0])]
    else:
        verticalMove = ['DOWN' for _ in range(0, princess[0] - bot[0])]

    if verticalMove:
        return verticalMove[0]

    if bot[1] > princess[1]:
        horizontalMove = ['LEFT' for _ in range(0, bot[1] - princess[1])]
    else:
        horizontalMove = ['RIGHT' for _ in range(0, princess[1] - bot[1])]

    if horizontalMove:
        return horizontalMove[0]

    return ""

