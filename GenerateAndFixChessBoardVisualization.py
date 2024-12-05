# Visualize the chessboard after the fixes are completed

import pygame

pygame.init()

WIDTH=800
HEIGHT=800
screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption('Generate and Fix Chessboard')

font = pygame.font.Font('freesansbold.ttf', 20)
medium_font = pygame.font.Font('freesansbold.ttf', 40)
big_font = pygame.font.Font('freesansbold.ttf', 50)

timer = pygame.time.Clock()
fps = 60

captured_pieces_white = []
captured_pieces_black = []

# 0 - whites turn no selection; 1-whites turn piece selected; 2- black turn no selection; 3 - black turn piece selected
turn_step = 0
selection = 100
valid_moves = []

# Piece and image loading
bqueen=pygame.image.load('./images/Chess_qdt60.png')
wqueen=pygame.image.load('./images/Chess_qlt60.png')
bking=pygame.image.load('./images/Chess_kdt60.png')
wking=pygame.image.load('./images/Chess_klt60.png')
bknight=pygame.image.load('./images/Chess_ndt60.png')
wknight=pygame.image.load('./images/Chess_nlt60.png')
brook=pygame.image.load('./images/Chess_rdt60.png')
wrook=pygame.image.load('./images/Chess_rlt60.png')
bpawn=pygame.image.load('./images/Chess_pdt60.png')
wpawn=pygame.image.load('./images/Chess_plt60.png')
bbishop=pygame.image.load('./images/Chess_bdt60.png')
wbishop=pygame.image.load('./images/Chess_blt60.png')

chessboard = {'a|1': 'bbishop',
 'a|4': 'wpawn',
 'a|6': 'wpawn',
 'b|2': 'wrook',
 'b|3': 'bpawn',
 'b|5': 'wpawn',
 'b|8': 'wknight',
 'c|1': 'wrook',
 'c|2': 'wrook',
 'c|5': 'bbishop',
 'c|7': 'wpawn',
 'c|8': 'wknight',
 'd|1': 'wpawn',
 'd|2': 'wrook',
 'd|3': 'wpawn',
 'd|4': 'bking',
 'd|6': 'brook',
 'd|7': 'bpawn',
 'e|1': 'bking',
 'e|7': 'wrook',
 'f|1': 'bqueen',
 'f|4': 'wpawn',
 'f|7': 'wpawn',
 'f|8': 'bking',
 'g|1': 'wqueen',
 'g|3': 'wpawn',
 'g|5': 'bpawn',
 'g|7': 'bpawn',
 'h|2': 'bking',
 'h|5': 'wpawn',
 'h|7': 'wknight'}

def drawBoard():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, 'light gray', [
                             600 - (column * 200), row * 100, 100, 100])
        else:
            pygame.draw.rect(screen, 'light gray', [
                             700 - (column * 200), row * 100, 100, 100])
        pygame.draw.rect(screen, 'gray', [0, 800, WIDTH, 100])
        pygame.draw.rect(screen, 'gold', [0, 800, WIDTH, 100], 5)
        pygame.draw.rect(screen, 'gold', [800, 0, 200, HEIGHT], 5)
        status_text = ['White: Select a Piece to Move!', 'White: Select a Destination!',
                       'Black: Select a Piece to Move!', 'Black: Select a Destination!']
        screen.blit(big_font.render(
            status_text[turn_step], True, 'black'), (20, 820))
        for i in range(9):
            pygame.draw.line(screen, 'black', (0, 100 * i), (800, 100 * i), 2)
            pygame.draw.line(screen, 'black', (100 * i, 0), (100 * i, 800), 2)
        screen.blit(medium_font.render('FORFEIT', True, 'black'), (810, 830))
        return

def drawPieces(chessboard):
    for pair in chessboard:
        coord = ((ord(pair[0])%32 - 1),int(pair[-1]) - 1)
        piece = chessboard[pair]
        return

def runVisualization(chessboard):
    while True:
        timer.tick(fps)
        screen.fill('dark gray')
        drawBoard()
        drawPieces(chessboard)

runVisualization(chessboard)