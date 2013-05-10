def displayPathtoPrincess(n, grid):
    bot = [0, 0]
    princess = [0, 0]
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == 'm':
                bot = (i, j)
            elif col == 'p':
                princess = (i, j)

    if bot[0] > princess[0]:
        verticalMove = ('UP' for _ in range(0, bot[0] - princess[0]))
    else:
        verticalMove = ('DOWN' for _ in range(0, princess[0] - bot[0]))

    if bot[1] > princess[1]:
        horizontalMove = ('LEFT' for _ in range(0, bot[1] - princess[1]))
    else:
        horizontalMove = ('RIGHT' for _ in range(0, princess[1] - bot[1]))

    print '\n'.join(verticalMove)
    print '\n'.join(horizontalMove)
