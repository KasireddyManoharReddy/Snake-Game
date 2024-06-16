import pygame,sys,random
from pygame.math import Vector2

class FRUIT:
    def __init__(self) -> None:
       self.randomize()

    def draw_fruit(self):
        f_rect = pygame.Rect(self.position.x*size,self.position.y*size,size,size)
        screen.blit(apple,f_rect)  

    def randomize(self):
        self.x =random.randint(0,number-1)
        self.y =random.randint(0,number-1)
        self.position = Vector2(self.x,self.y)     


class SNAKE:
    def __init__(self):
        self.body =[Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0,0)
        self.cond = False
        self.snake_hu = pygame.image.load("Graphics/head_up.png").convert_alpha()
        self.snake_hd = pygame.image.load("Graphics/head_down.png").convert_alpha()
        self.snake_hr = pygame.image.load("Graphics/head_right.png").convert_alpha()
        self.snake_hl = pygame.image.load("Graphics/head_left.png").convert_alpha()
        self.snake_tu = pygame.image.load("Graphics/tail_up.png").convert_alpha()
        self.snake_td = pygame.image.load("Graphics/tail_down.png").convert_alpha()
        self.snake_tr = pygame.image.load("Graphics/tail_right.png").convert_alpha()
        self.snake_tl = pygame.image.load("Graphics/tail_left.png").convert_alpha()
        self.snake_bv = pygame.image.load("Graphics/body_vertical.png").convert_alpha()
        self.snake_bh = pygame.image.load("Graphics/body_horizontal.png").convert_alpha()
        self.snake_btr = pygame.image.load("Graphics/body_tr.png").convert_alpha()
        self.snake_btl = pygame.image.load("Graphics/body_tl.png").convert_alpha()
        self.snake_bbr = pygame.image.load("Graphics/body_br.png").convert_alpha()
        self.snake_bbl = pygame.image.load("Graphics/body_bl.png").convert_alpha()
        self.sound = pygame.mixer.Sound("Sound/crunch.wav")

    def draw_snake(self):
        self.snake_head()
        self.snake_tail()
        for index,point in enumerate(self.body):
          s_rect = pygame.Rect(point.x*size,point.y*size,size,size)
          if index ==0:
              screen.blit(self.head,s_rect)
          elif index ==len(self.body)-1:
              screen.blit(self.tail,s_rect) 
          else:
              p_block = self.body[index+1]-point 
              n_block = self.body[index-1]-point
              if p_block.x==n_block.x:
                  screen.blit(self.snake_bv,s_rect) 
              elif  p_block.y==n_block.y:   
                  screen.blit(self.snake_bh,s_rect)
              else:
                  if p_block.x==-1 and n_block.y==-1 or p_block.y==-1 and n_block.x==-1:
                      screen.blit(self.snake_btl,s_rect) 
                  elif p_block.x==-1 and n_block.y==1 or p_block.y==1 and n_block.x==-1:
                      screen.blit(self.snake_bbl,s_rect) 
                  elif p_block.x==1 and n_block.y==-1 or p_block.y==-1 and n_block.x==1:
                      screen.blit(self.snake_btr,s_rect) 
                  elif p_block.x==1 and n_block.y==1 or p_block.y==1 and n_block.x==1:
                      screen.blit(self.snake_bbr,s_rect)                
          
                 


    def snake_head(self):
        head_r = self.body[1]-self.body[0]
        if head_r == Vector2(1,0):self.head = self.snake_hl   
        if head_r == Vector2(-1,0):self.head = self.snake_hr  
        if head_r == Vector2(0,1):self.head = self.snake_hu
        if head_r == Vector2(0,-1):self.head = self.snake_hd 


    def snake_tail(self):
        head_r = self.body[len(self.body)-1]-self.body[len(self.body)-2]
        if head_r == Vector2(1,0):self.tail = self.snake_tr   
        if head_r == Vector2(-1,0):self.tail = self.snake_tl
        if head_r == Vector2(0,1):self.tail = self.snake_td
        if head_r == Vector2(0,-1):self.tail = self.snake_tu    

    def move_snake(self):
        if self.cond==True:
           b_copy = self.body[:]
           b_copy.insert(0,self.body[0]+self.direction)
           self.body = b_copy[:]
           self.cond =False
        else:
           b_copy = self.body[:-1]
           b_copy.insert(0,self.body[0]+self.direction)
           self.body = b_copy[:]    

    def add_block(self):
        self.cond =True

    def play_sound(self):
        self.sound.play()   

    def reset(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0,0)
        


class MAIN:
    def __init__(self) -> None:
           self.snake = SNAKE()
           self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()
        self.collision()

    def draw(self):    
        self.fruit.draw_fruit()   
        self.snake.draw_snake()
        self.draw_score()
        self.fail()
        

    def collision(self):
        if self.fruit.position == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_sound()

        for block in self.snake.body[1:]:
            if block == self.fruit.position:
                self.fruit.randomize()

    def fail(self):
        if not 0<= self.snake.body[0].x<number or not 0<= self.snake.body[0].y<number:
               self.game_over()
        for point in self.snake.body[1:]:
            if point == self.snake.body[0]:
                self.game_over()         

    def game_over(self):
            self.snake.reset() 

    def draw_score(self): 
        score_t = "Score:"+str(len(self.snake.body)-3)
        score_s = game_font.render(score_t,True,(56,74,12))  
        score_r = score_s.get_rect(center =(size*number-60,size*number-40))     
        bg_rect =pygame.Rect(score_r.left-5,score_r.top,score_r.width+10,score_r.height)
        pygame.draw.rect(screen,(167,209,61),bg_rect)
        screen.blit(score_s,score_r)
        pygame.draw.rect(screen,(56,74,12),bg_rect,2)    

pygame.init()
size =40
number = 20

screen = pygame.display.set_mode((size*number,size*number))
clock = pygame.time.Clock()
main =MAIN()
apple = pygame.image.load("Graphics/apple.png").convert_alpha()
game_font = pygame.font.Font("Font/font1.ttf",25)
S_UPDATE = pygame.USEREVENT
pygame.time.set_timer(S_UPDATE,150)
#surface1 = pygame.Surface((100,200))

while(True):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==S_UPDATE:
            main.update()   

        if event.type ==pygame.KEYDOWN:
            
            if event.key == pygame.K_UP:
                if main.snake.direction.y!=1:
                 main.snake.direction =Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                if main.snake.direction.y!=-1:
                 main.snake.direction =Vector2(0,+1)        
            if event.key == pygame.K_RIGHT:
                if main.snake.direction.x!=-1:
                 main.snake.direction =Vector2(+1,0)
            if event.key == pygame.K_LEFT:
                if main.snake.direction.x!=1:
                  main.snake.direction =Vector2(-1,0)       

    screen.fill((175,215,70))   
    main.draw()
    pygame.display.update()
    clock.tick(60)
