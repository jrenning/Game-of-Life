import pygame
import random 
import numpy as np





class Window():
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.display = pygame.display.set_mode((width,height))

class GameOfLIfe():
    def __init__(self,window: Window,board,clock,speed):
        self.window = window
        self.board = board
        self.clock = clock
        self.speed = speed
    def run_game_loop(self):
        game_over = False
        # randomize starting board
        self.randomize_board()
        while not game_over: 

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
            self.update_game_board()      
            self.draw_game_board()
            pygame.display.update()
            
            self.clock.tick(self.speed)
    
    def randomize_board(self):
        
        for i,row in enumerate(self.board):
            for j,_ in enumerate(row):
                random_num = random.random()
                if random_num < 0.5:
                    self.board[i][j] = 0
                else:
                    self.board[i][j] = 1
                    
    def update_game_board(self):
        
        for i,row in enumerate(self.board):
            for j,life in enumerate(row):
                if life == 1:
                    # if alive and has two neighbors die
                    if self.get_live_neighbors(j,i) < 2:
                        self.board[i][j] = 0
                    # if alive and has 2 oe 3 neighbors keep alive 
                    # if alive and has more than 3 live neighbors dies from overpopulation
                    if self.get_live_neighbors(j,i) > 3:
                        self.board[i][j] = 0
                if life == 0:
                    # if dead cell has exactly three neighbors bring it to life 
                    if self.get_live_neighbors(j,i) == 3:
                        self.board[i][j] = 1
                        
                # random life generation (makes the thing continuous )
                if random.randint(0,25000) == 0:
                    self.board[i][j] = 1

                        
                    
                        
                    
    def get_live_neighbors(self,x_index, y_index):
        live_neighbors = 0
        
        # width of the board index
        h = len(self.board)-1
        # height of board index
        w = len(self.board[0])-1
        
        # if x index is 0 don't check left 
        # if y index is 0 dont check above 
        # if x index is width dont check right 
        # if y index is height dont check down 
        
        if x_index != 0:
            if self.board[y_index][x_index-1] == 1:
                live_neighbors += 1
            if y_index != h:
                if self.board[y_index+1][x_index-1] == 1:
                    live_neighbors += 1
            if y_index != 0:
                if self.board[y_index-1][x_index-1] == 1:
                    live_neighbors += 1
        
        if x_index != w:
            if self.board[y_index][x_index+1] == 1:
                live_neighbors += 1
            if y_index != 0:
                if self.board[y_index-1][x_index+1] == 1:
                    live_neighbors += 1
            if y_index != h:
                if self.board[y_index-1][x_index+1] == 1:
                    live_neighbors += 1
        
        if y_index != 0:
            if self.board[y_index-1][x_index] == 1:
                live_neighbors += 1
        if y_index != h:
            if self.board[y_index+1][x_index] == 1:
                live_neighbors += 1

        
        return live_neighbors            
            
    def draw_game_board(self):
        # width of the board
        h = len(self.board)
        # height of board
        w = len(self.board[0])
        # width of each hunk
        x_chunk = self.window.width // w
        # height of each chunk
        y_chunk = self.window.height // h
        
        random_color = (random.random()*255, random.random()*255, random.random()*255)
        
        #random_color = (100,100,100)
        
        for i,row in enumerate(self.board):
            for j,life in enumerate(row):
                if life == 1:
                    pygame.draw.rect(self.window.display,random_color,[j*x_chunk,i*y_chunk,x_chunk-1,y_chunk-1])
                else:
                    pygame.draw.rect(self.window.display,(0,0,0),[j*x_chunk,i*y_chunk,x_chunk-1,y_chunk-1])
            
            
                
    
                
        
        
        

def main():
    pygame.init()
    clock = pygame.time.Clock()
    speed = 15
    window = Window(800,1200)
    # initial board of all zeros 
    board = np.zeros((200,200))
    game = GameOfLIfe(window,board,clock,speed)
    
    game.run_game_loop()
    

if __name__ == "__main__":
    main()
    


