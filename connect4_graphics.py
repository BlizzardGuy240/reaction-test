import numpy as np
import pygame
import sys
import math as m
import random

row_count = 6
column_count = 7

def create_board():
    board = np.zeros((row_count, column_count))
    return board

def drop_piece(baord, row, col, piece):
    board[row][col] = piece

def is_valid_loc(board, col):
    return board[row_count - 1][col] == 0

def get_open_row(board, col):
    for r in range(row_count):
        if board[r][col] == 0:
            return r

def win_move(board, piece):
   # HORIZONTAL CONDITION:
    for c in range(column_count - 3):
        for r in range(row_count):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
            
    # VERTICAL CONDITION:
    for c in range(column_count):
        for r in range(row_count - 3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
        
    # + DIAGONALS CONDITION:
    for c in range(column_count - 3):
        for r in range(row_count - 3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # - DIAGONALS CONDITION:
    for c in range(column_count - 3):
        for r in range(3, row_count):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True
            
def draw_board(board):
    pygame.draw.rect(screen, (0, 0, 255), (0, size_square, size_square * (row_count + 1), size_square * column_count))
    for c in range(column_count):
        for r in range(row_count):
            pygame.draw.circle(screen, (0, 0, 0), (c*size_square + int(size_square/2), r*size_square + size_square + int(size_square/2)) , (int(size_square/2 - 5)))
            
    for c in range(column_count):
            for r in range(row_count):
                if board[r][c] == 1:
                    pygame.draw.circle(screen, (255, 0, 0), (c*size_square + int(size_square/2), height - (r*size_square + int(size_square/2))) , (int(size_square/2 - 5)))
                elif board[r][c] == 2:
                    pygame.draw.circle(screen, (255, 255, 0), (c*size_square + int(size_square/2), height - (r*size_square + int(size_square/2))) , (int(size_square/2 - 5)))
    pygame.display.update()

board = create_board()
game_over = False
turn = random.randint(0, 1)

pygame.init()

size_square = 100

size = (column_count * size_square, (row_count + 1) * size_square)
height = size[1]
width = size[0]

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Connect 4")


draw_board(board)


while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, (0, 0, 0), (0, 0, width, size_square))
            posx = event.pos[0]

            if turn == 0:
                pygame.draw.circle(screen, (255, 0, 0), (posx, int(size_square/2)), int(size_square/2 - 5))
            elif turn == 1:
                pygame.draw.circle(screen, (255, 255, 0), (posx, int(size_square/2)), int(size_square/2 - 5))

        pygame.display.update()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, (0, 0, 0), (0, 0, width, size_square))
                        
            # PLAYER ONE
            if turn == 0:
                col = int(m.floor(event.pos[0]/size_square))
                                
                if is_valid_loc(board, col):
                    row = get_open_row(board, col)
                    drop_piece(board, row, col, 1)

                    if win_move(board, 1):
                        label = pygame.font.SysFont("monospace", 70).render("PLAYER ONE WINS!", 1, (255, 0, 0))
                        screen.blit(label, (20, 10))
                        game_over = True
            
            # PLAYER TWO:
            else:
                col = int(m.floor(event.pos[0]/size_square))

                if is_valid_loc(board, col):
                    row = get_open_row(board, col)
                    drop_piece(board, row, col, 2)

                    if win_move(board, 2):
                        label = pygame.font.SysFont("monospace", 70).render("PLAYER TWO WINS!", 1, (255, 255, 0))
                        screen.blit(label, (20, 10))
                        game_over = True
            

            turn += 1
            turn = turn % 2
            # print_board(board)
            draw_board(board)

            if game_over:
                pygame.time.wait(3000)
            
