import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 400, 430
LINE_WIDTH = 6
BOARD_ROWS, BOARD_COLS = 3, 3
CELL_SIZE = 100
BOARD_WIDTH = CELL_SIZE * BOARD_COLS
BOARD_HEIGHT = CELL_SIZE * BOARD_ROWS
BOARD_X = (WIDTH - BOARD_WIDTH) // 2
BOARD_Y = (HEIGHT - BOARD_HEIGHT) // 2

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LINE_COLOR = (23, 145, 135)
BG_COLOR = (236, 236, 236)
TEXT = (0, 128, 0)
WARNING_TEXT=(255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BG_COLOR)

# Create Tic Tac Toe board
board = [['' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

# Draw the lines of the Tic Tac Toe grid
def draw_lines():
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(screen, LINE_COLOR, (BOARD_X, BOARD_Y + i * CELL_SIZE),
                         (BOARD_X + BOARD_WIDTH, BOARD_Y + i * CELL_SIZE), LINE_WIDTH)
    for i in range(1, BOARD_COLS):
        pygame.draw.line(screen, LINE_COLOR, (BOARD_X + i * CELL_SIZE, BOARD_Y),
                         (BOARD_X + i * CELL_SIZE, BOARD_Y + BOARD_HEIGHT), LINE_WIDTH)

# Draw X and O on the board
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'X':
                pygame.draw.line(screen, BLACK, (BOARD_X + col * CELL_SIZE + 20, BOARD_Y + row * CELL_SIZE + 20),
                                 (BOARD_X + (col + 1) * CELL_SIZE - 20, BOARD_Y + (row + 1) * CELL_SIZE - 20), LINE_WIDTH)
                pygame.draw.line(screen, BLACK, (BOARD_X + (col + 1) * CELL_SIZE - 20, BOARD_Y + row * CELL_SIZE + 20),
                                 (BOARD_X + col * CELL_SIZE + 20, BOARD_Y + (row + 1) * CELL_SIZE - 20), LINE_WIDTH)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, BLACK, (BOARD_X + col * CELL_SIZE + CELL_SIZE // 2, BOARD_Y + row * CELL_SIZE + CELL_SIZE // 2),
                                   CELL_SIZE // 2 - 20, LINE_WIDTH)

# Check for a winner
def check_winner():
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] != '':
            return board[row][0]
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] != '':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '':
        return board[0][2]
    return None

# Check if the board is full
def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == '':
                return False
    return True

# Display whose turn it is
def display_turn(turn):
    font = pygame.font.SysFont(None, 30)
    text = font.render(f"Player {turn}'s turn", True, BLACK)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT - 40))
    screen.blit(text, text_rect)

# Main game loop
def main():
    turn = 'X'
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouseX = (event.pos[0] - BOARD_X) // CELL_SIZE
                mouseY = (event.pos[1] - BOARD_Y) // CELL_SIZE

                if 0 <= mouseX < BOARD_COLS and 0 <= mouseY < BOARD_ROWS and board[mouseY][mouseX] == '':
                    board[mouseY][mouseX] = turn
                    if turn == 'X':
                        turn = 'O'
                    else:
                        turn = 'X'

        screen.fill(BG_COLOR)
        pygame.draw.rect(screen, BLACK, (BOARD_X - 3, BOARD_Y - 3, BOARD_WIDTH + 6, BOARD_HEIGHT + 6), 3)
        draw_lines()
        draw_figures()
        display_turn(turn)

        if check_winner() is not None:
            winner = check_winner()
            font = pygame.font.SysFont(None, 50)
            text = font.render(f"Player {winner} wins!", True, TEXT)
            screen.blit(text, ((WIDTH - text.get_width()) // 2, (HEIGHT - text.get_height()) // 1))
            game_over = True
        elif is_board_full():
            font = pygame.font.SysFont(None, 50)
            text = font.render("It's a tie!", True, WARNING_TEXT)
            screen.blit(text, ((WIDTH - text.get_width()) // 2, (HEIGHT - text.get_height()) // 1))
            game_over = True

        pygame.display.update()

        if game_over:
            pygame.time.wait(3000)

if __name__ == "__main__":
    main()
