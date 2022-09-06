
import pygame, sys, os, random
from pygame.locals import QUIT, KEYDOWN, K_SPACE


def img_rescale(path: str, dimension: tuple[int]):
    return pygame.transform.scale(pygame.image.load(os.path.join('Python\Project Floppy Bird\Resources', path)), dimension)


WIDTH = 540
HEIGHT = 720

CHAR_IMG = [img_rescale(f'char_fly_{i}.png', (80, 80)) for i in range(8)]  # 500 x 500
CHAR_FALL_IMG = [img_rescale(f'char_fall_{i}.png', (80, 80)) for i in range(20)]   # 500 x 500
NUM_IMG = [img_rescale(f'{i}w.png', (50, 50)) for i in range(10)]   # 500 x 500
ICON_IMG = img_rescale('icon.png', (500, 500))   # 500 x 500
PIPE_IMG = img_rescale('pipe.png', (90, 540))  # 250 x 1500
BASE_IMG = img_rescale('base.png', (540, 40))   # 540 x 40
BACKGROUND_IMG = img_rescale('background.png', (540, 720))   # 540 x 720

OFFWHITE = (242, 243, 244)

FPS = 60


class Char:
    MAX_ROTATION = 20
    ROTATE_VELOCITY = 5
    ANIMATION_TIME = 5

    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.pos_y   # tmp
        self.img_count = 0
        self.img = CHAR_IMG[0]

    def jump(self):
        self.vel = -15
        self.height = self.pos_y
        self.tick_count = 0   # keep track of last jump

        self.pos_y += self.vel

    def move(self):
        self.tick_count += 1   # for each frame

        displacement = int(self.vel*self.tick_count + 1.5*self.tick_count**2)//30  # (pixels) keep track of up/down movements
        if displacement >= 15:   # terminal velocity
            displacement = 15   
        if displacement < 0:   # fine-tune char movements
            displacement -= 2

        self.pos_y += displacement

        if displacement < 0 or self.pos_y < self.height + 50:   # tilt upwards
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:   # tilt downwards
            if self.tilt > -90:
                self.tilt -= self.ROTATE_VELOCITY
    
    def draw(self, window: pygame.Surface, isOver: bool):
        self.img_count += 1

        if not isOver:
            # inefficient
            if self.img_count < self.ANIMATION_TIME:
                self.img = CHAR_IMG[0]
            elif self.img_count < self.ANIMATION_TIME*2:
                self.img = CHAR_IMG[1]
            elif self.img_count < self.ANIMATION_TIME*3:
                self.img = CHAR_IMG[2]
            elif self.img_count < self.ANIMATION_TIME*4:
                self.img = CHAR_IMG[3]
            elif self.img_count < self.ANIMATION_TIME*5:
                self.img = CHAR_IMG[4]
            elif self.img_count < self.ANIMATION_TIME*6:
                self.img = CHAR_IMG[5]
            elif self.img_count < self.ANIMATION_TIME*7:
                self.img = CHAR_IMG[6]
            elif self.img_count < self.ANIMATION_TIME*8:
                self.img = CHAR_IMG[7]
            elif self.img_count < self.ANIMATION_TIME*8 + 1:
                self.img = CHAR_IMG[0]
                self.img_count = 0

            if self.tilt <= -80:
                self.img = CHAR_IMG[0]
                self.img_count = self.ANIMATION_TIME

            # rotates char around center, copied from stackoverflow, no idea what it does
            rotated_img = pygame.transform.rotate(self.img, self.tilt)
            new_rect = rotated_img.get_rect(center=self.img.get_rect(topleft=(self.pos_x, self.pos_y)).center)
            window.blit(rotated_img, new_rect.topleft)
        
        else:
            if self.img_count < self.ANIMATION_TIME:
                self.img = CHAR_FALL_IMG[0]
            elif self.img_count < self.ANIMATION_TIME*2:
                self.img = CHAR_FALL_IMG[1]
            elif self.img_count < self.ANIMATION_TIME*3:
                self.img = CHAR_FALL_IMG[2]
            elif self.img_count < self.ANIMATION_TIME*4:
                self.img = CHAR_FALL_IMG[3]
            elif self.img_count < self.ANIMATION_TIME*5:
                self.img = CHAR_FALL_IMG[4]
            elif self.img_count < self.ANIMATION_TIME*6:
                self.img = CHAR_FALL_IMG[3]
            elif self.img_count < self.ANIMATION_TIME*7:
                self.img = CHAR_FALL_IMG[2]
            elif self.img_count < self.ANIMATION_TIME*8:
                self.img = CHAR_FALL_IMG[1]
            elif self.img_count < self.ANIMATION_TIME*9:
                self.img = CHAR_FALL_IMG[0]
            elif self.img_count < self.ANIMATION_TIME*10:
                self.img = CHAR_FALL_IMG[1]
            elif self.img_count < self.ANIMATION_TIME*11:
                self.img = CHAR_FALL_IMG[2]
            elif self.img_count < self.ANIMATION_TIME*12:
                self.img = CHAR_FALL_IMG[3]
            elif self.img_count < self.ANIMATION_TIME*13:
                self.img = CHAR_FALL_IMG[4]
            elif self.img_count < self.ANIMATION_TIME*14:
                self.img = CHAR_FALL_IMG[5]
            elif self.img_count < self.ANIMATION_TIME*15:
                self.img = CHAR_FALL_IMG[6]
            elif self.img_count < self.ANIMATION_TIME*16:
                self.img = CHAR_FALL_IMG[7]
            elif self.img_count < self.ANIMATION_TIME*17:
                self.img = CHAR_FALL_IMG[8]
            elif self.img_count < self.ANIMATION_TIME*18:
                self.img = CHAR_FALL_IMG[9]
            elif self.img_count < self.ANIMATION_TIME*19:
                self.img = CHAR_FALL_IMG[10]
            elif self.img_count < self.ANIMATION_TIME*20:
                self.img = CHAR_FALL_IMG[11]
            elif self.img_count < self.ANIMATION_TIME*21:
                self.img = CHAR_FALL_IMG[12]
            elif self.img_count < self.ANIMATION_TIME*22:
                self.img = CHAR_FALL_IMG[13]
            elif self.img_count < self.ANIMATION_TIME*23:
                self.img = CHAR_FALL_IMG[14]
            elif self.img_count < self.ANIMATION_TIME*24:
                self.img = CHAR_FALL_IMG[15]
            elif self.img_count < self.ANIMATION_TIME*25:
                self.img = CHAR_FALL_IMG[16]
            elif self.img_count < self.ANIMATION_TIME*26:
                self.img = CHAR_FALL_IMG[17]
            elif self.img_count < self.ANIMATION_TIME*27:
                self.img = CHAR_FALL_IMG[18]
            elif self.img_count < self.ANIMATION_TIME*27 + 1:
                self.img = CHAR_FALL_IMG[19]
            
            opacity = self.img_count*2
            if opacity > 255:
                opacity = 255

            fadeout = window.convert()
            fadeout.fill((0, 0, 0))
            fadeout.set_alpha(opacity)

            window.blit(fadeout, (0, 0))
            window.blit(self.img, (self.pos_x, self.pos_y))

    def get_mask(self):   # for pixel-perfect collision detection
        return pygame.mask.from_surface(self.img)


class Pipe:
    DISTANCE = 150
    VELOCITY = 5
    PIPE_TOP = pygame.transform.flip(PIPE_IMG, flip_x=False, flip_y=True)
    PIPE_BOTTOM = PIPE_IMG

    def __init__(self, pos_x):
        self.pos_x = pos_x
        self.height = 0
        self.pos_y_top = 0
        self.pos_y_bottom = 0

        self.passed = False

        self.set_height()

    def set_height(self):
        self.height = random.randrange(30, 380)
        self.pos_y_top = self.height - self.PIPE_TOP.get_height()
        self.pos_y_bottom = self.height + self.DISTANCE

    def move(self):
        self.pos_x -= self.VELOCITY
    
    def draw(self, window: pygame.Surface):
        window.blit(self.PIPE_TOP, (self.pos_x, self.pos_y_top))
        window.blit(self.PIPE_BOTTOM, (self.pos_x, self.pos_y_bottom))

    def collide(self, char: Char) -> bool:
        char_mask = char.get_mask()
        pipe_top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        pipe_bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)

        # distance between those masks
        pipe_top_offset = (self.pos_x - char.pos_x, self.pos_y_top - round(char.pos_y))
        pipe_bottom_offset = (self.pos_x - char.pos_x, self.pos_y_bottom - round(char.pos_y))

        # check if those masks collide
        top_point = char_mask.overlap(pipe_top_mask, pipe_top_offset)
        bottom_point = char_mask.overlap(pipe_bottom_mask, pipe_bottom_offset)

        # check if a collision point exists
        if top_point or bottom_point:   # is not None
            return True
        return False


class Base:
    VELOCITY = 6
    WIDTH = BASE_IMG.get_width()

    def __init__(self, pos_y):
        self.pos_y = pos_y
        self.pos_x1 = 0
        self.pos_x2 = self.WIDTH

    def move(self):
        self.pos_x1 -= self.VELOCITY
        self.pos_x2 -= self.VELOCITY

        # infinitely loop 2 instances of BASE_IMG
        if self.pos_x1 + self.WIDTH < 0:
            self.pos_x1 = self.pos_x2 + self.WIDTH
        if self.pos_x2 + self.WIDTH < 0:
            self.pos_x2 = self.pos_x1 + self.WIDTH

    def draw(self, window: pygame.Surface):
        window.blit(BASE_IMG, (self.pos_x1, self.pos_y))
        window.blit(BASE_IMG, (self.pos_x2, self.pos_y))


class Score:
    def __init__(self, pos_x, pos_y, slot):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.slot = slot    # [0, 1, 2]

    def draw(self, window: pygame.Surface, score: int):
        text = int(f'{score:03d}'[self.slot])
        window.blit(NUM_IMG[text], (self.pos_x, self.pos_y))


class App():
    def draw_window(self, window: pygame.Surface, char: Char, pipes: list[Pipe], base: Base, score: int, scoreslots: list[Score], isOver: bool):
        window.blit(BACKGROUND_IMG, (0, 0))

        for pipe in pipes:
            pipe.draw(window)

        if not isOver:
            for scoreslot in scoreslots:
                scoreslot.draw(window, score=score)
        
        base.draw(window)
        char.draw(window, isOver)

        pygame.display.update()

    def draw_window_end(self, window: pygame.Surface, cont, countdown: Score, y_butt, n_butt):
        ...

    def main(self):
        pygame.display.set_caption('trojan.exe')
        pygame.display.set_icon(ICON_IMG)

        self.FPS_clock = pygame.time.Clock()

        self.char = Char(150, 250)
        self.pipes = [Pipe(540)]
        self.base = Base(680)

        self.score = 0
        self.scoreslot_0 = Score(210, 135, 0)
        self.scoreslot_1 = Score(245, 135, 1)
        self.scoreslot_2 = Score(280, 135, 2)

        # flow: self.isStarted -> self.isOver
        self.isStarted = False
        self.isOver = False

        while True:
            self.FPS_clock.tick(FPS)

            if not self.isStarted or self.isOver:
                for pipe in self.pipes:
                    pipe.VELOCITY = 0
                self.base.VELOCITY = 0
            
            if not self.isOver:
                self.base.VELOCITY = Base(...).VELOCITY
                if self.isStarted:
                    for pipe in self.pipes:
                        pipe.VELOCITY = Pipe(540).VELOCITY
                    self.base.VELOCITY = Base(...).VELOCITY
                    self.char.move()

            self.window = pygame.display.set_mode((WIDTH, HEIGHT))
            self.window.fill(OFFWHITE)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if not self.isOver:
                    if event.type == KEYDOWN:
                        self.isStarted = True
                        if event.key == K_SPACE and not self.isOver:
                            self.char.jump()
                
            add_pipe = False

            for pipe in self.pipes:
                if pipe.collide(self.char):
                    self.isStarted = False
                    self.isOver = True
                if not pipe.passed and pipe.pos_x < self.char.pos_x:
                    pipe.passed = True
                    add_pipe = True
                pipe.move()

            if add_pipe:
                self.score += 1
                self.pipes.append(Pipe(540))

            if self.char.pos_y + self.char.img.get_height() >= 680:   # hit the floor
                self.isStarted = False
                self.isOver = True
            elif self.char.pos_y < -20:   # hit the sky
                self.isStarted = False
                self.isOver = True

            self.base.move()
            
            self.draw_window(self.window, self.char, self.pipes, self.base, self.score, [self.scoreslot_0, self.scoreslot_1, self.scoreslot_2], self.isOver)
                
            pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    app = App()
    app.main()


"""
CREDIT:
- Character images: https://www.deviantart.com/packedice/art/falling-raccoon-860675801
- Background image: https://pixelart.io/uploads/2018-12-06/pixelart_1544126349514.png
- Pipe image & Base image: v.a.
"""