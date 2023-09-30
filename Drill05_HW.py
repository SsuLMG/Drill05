from pico2d import *
import random


TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('rockman.png')
arrow = load_image('hand_arrow.png')

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
cursor_x, cursor_y = TUK_WIDTH // 2, TUK_HEIGHT // 2

def Lerp(A, B, Alpha):
    return A * (1 - Alpha) + B * Alpha

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    x = Lerp(x, cursor_x, 0.1)
    y = Lerp(y, cursor_y, 0.1)

    if(cursor_x > x):
        character.clip_draw(frame * 172, 0, 172, 183, x, y, 100, 100)
    elif(cursor_x < x):
        character.clip_composite_draw(frame * 172, 0, 172, 183, 0, 'h', x, y, 100, 100)


    arrow.draw_now(cursor_x, cursor_y)

    update_canvas()
    frame = (frame + 1) % 8

    if(cursor_x - 10 < x < cursor_x + 10 and cursor_y - 10 < y < cursor_y + 10):
        cursor_x = random.randint(100, 1000)
        cursor_y = random.randint(100, 800)

    delay(0.05)

close_canvas()