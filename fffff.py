from tkinter import * 
import random 
 
window = Tk() 
w = 600 
h = 600 
window.geometry(f'{w}x{h}') 
 
canvas = Canvas(window, width=w, height=h) 
canvas.place(in_=window, x=0, y=0) 
bg_photo = PhotoImage(file='bg_2.png') 
 
 
 
class Knight: 
 
    def __init__(self): 
        self.x = 70 
        self.y = h // 2 
        self.v = 0 
        self.v_x = 0 
        self.photo = PhotoImage(file='knight.png') 
 
    def up(self, event): 
        self.v = -3 
 
    def down(self, event): 
        self.v = +3 
 
    def right(self, event): 
        self.v_x = +3 
 
    def left(self, event): 
        self.v_x = -3 
 
    def stop_all(self, event): 
        self.v = 0 
        self.v_x = 0 
 
 
class Dragon: 
    def __init__(self): 
        self.x = random.randint(700, 1500) 
        self.y = random.randint(100, 500) 
        self.v = random.randint(1, 3) 
        self.photo = PhotoImage(file='dragon.png') 
 
 
knight = Knight() 
dragons = [] 
for i in range(10): 
    dragons.append(Dragon()) 
 
 
def game(): 
    canvas.delete('all') 
    canvas.create_image(h // 2, w // 2, image=bg_photo) 
    canvas.create_image(knight.x, knight.y, image=knight.photo) 
    knight.y += knight.v 
    knight.x += knight.v_x 
    canvas.create_image(knight.x, knight.y, image=knight.photo) 
    kill_dragon = -1 
    for i, dragon in enumerate(dragons): 
        dragon.x -= dragon.v 
        canvas.create_image(dragon.x, dragon.y, image=dragon.photo) 
 
        if ((dragon.x - knight.x) ** 2 + (dragon.y - knight.y) ** 2) <= 95 ** 2: 
            kill_dragon = i 
        if dragon.x <= 0: 
            canvas.delete('all') 
            canvas.create_text(w // 2.3, h // 2.3, text='you lose ', font='System 42', fill='red') 
            break 
 
    if kill_dragon > -1: 
        del dragons[kill_dragon] 
 
    if len(dragons) == 0: 
        canvas.delete('all') 
        canvas.create_text(w // 2, h // 2, text='gg you win', font='System 42', fill='red') 
 
    if knight.y <= 52: 
        knight.y = 53 
    if knight.y >= 544: 
        knight.y = 543 
    if knight.x <= 50: 
        knight.x = 51 
    if knight.x >= 550: 
        knight.x = 551 
    window.after(5, game) 
 
window.bind('<Key-Up>', knight.up) 
window.bind('<Key-Down>', knight.down) 
window.bind('<Key-Right>', knight.right) 
window.bind('<Key-Left>', knight.left) 
window.bind('<KeyRelease>', knight.stop_all) 
 
window.resizable(height=False, width=False) 
window.mainloop()