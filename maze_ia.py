#!/usr/bin/env python3
import sys
from sys import stdin
import time


def get_maze():
    maze = []
    line = stdin.readline()
    while '#' in line:
        maze.append(list(line))
        line = stdin.readline()
    return maze


def getaway_wall(get_maze, A_pos):
    valid_list = []
    lis = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for [x_bonus, y_bonus] in lis:
        if get_maze[A_pos[1] + y_bonus][A_pos[0] + x_bonus] in ['!', 'o', ' ']:
            valid_list.append(((A_pos[0] + x_bonus), (A_pos[1] + y_bonus)))
    return valid_list


def get_position(get_maze, name):
    lis_A_position = []
    for y in range(len(get_maze) - 1):
        for x in range(len(get_maze[y]) - 1):
            if get_maze[y][x] == name:
                lis_A_position.append([x, y])
    return lis_A_position


def choosing_valid_spot(A_pos, valid_box):
    x1 = valid_box[0][0] - A_pos[0]
    x2 = valid_box[0][1] - A_pos[1]
    return (x1, x2)


def BFS_Finding_Path(A_pos, maze):
    waiting_list = [[A_pos]]
    checked_list = set(A_pos)
    while waiting_list:
        route = waiting_list.pop(0)
        valid_list = getaway_wall(maze, route[-1])
        for i in valid_list:
            if i not in checked_list:
                checked_list.add(i)
                if maze[i[1]][i[0]] is '!':
                    if len(route) + 1 <= 20:
                        return route + [i]
                elif maze[i[1]][i[0]] is 'o':
                    return route + [i]
                waiting_list.append(route + [i])


def giving_direction(list_of_route, A_pos, valid_list):
    dic = {(1, 0): 'RIGHT', (-1, 0): 'LEFT', (0, 1): 'DOWN', (0, -1): 'UP'}
    step = []
    if list_of_route is not None:
        for i in range(len(list_of_route) - 1):
            x1 = list_of_route[i+1][0] - list_of_route[i][0]
            y1 = list_of_route[i+1][1] - list_of_route[i][1]
            step.append(dic[(x1, y1)])
        a = step.pop(0)

        return a

    return(dic[choosing_valid_spot(A_pos, valid_list)])


if __name__ == '__main__':
    for line in sys.stdin:
        start = time.time()
        if 'HELLO' in line:
            sys.stdout.write('I AM BAO\n\n')
        if 'YOU ARE' in line:
            sys.stdout.write('OK\n\n')
            name = str(line[-2])
        if 'MAZE' in line:
            maze = get_maze()
            A_pos = get_position(maze, name)[0]
            valid_list = getaway_wall(maze, A_pos)
            list_of_route = BFS_Finding_Path(A_pos, maze)
            f = open("hehe", "a")
            f.write(str(list_of_route)+'\n')
            f.close()
            step = giving_direction(list_of_route, A_pos, valid_list)
            sys.stdout.write('MOVE '+str(step)+'\n\n')
            sys.stderr.write(str(time.time()-start)+'\n\n')
