


def Main():
    tax = 6.5
    tip = 5 + tax
    print(tip)


Main()






# ##--------------------------------------------------------------
# import ctypes
# import time
# from time import time as temps
# from ctypes import windll, Structure, c_long, byref
# from PIL import ImageGrab
# from pynput.keyboard import Key, Controller
# import os
# from PIL import Image
# ##--------------------------------------------------------------

# class POINT(Structure):
#     _fields_ = [("x", c_long), ("y", c_long)]
    
# def Get():
#     pt = POINT()
#     windll.user32.GetCursorPos(byref(pt))
#     return([pt.x,pt.y])

# def pos(x,y):
#     ctypes.windll.user32.SetCursorPos(x, y)

# def click():
#     ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
#     ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up

# def Screen():
#         snapshot = ImageGrab.grab(bbox=(650,308,710,310))
#         save_path = "C:/Users/theot/Desktop/Dino Python/shot.jpg"
#         snapshot.save(save_path)

# def TestPix(x,y,img):
#     r,g,b = img.getpixel((x,y))
#     if (r < 100):
#         return 1
#     return 0

# def TestPixMult(x,y,n,img):
#     r = 0
#     g = 0
#     b = 0
#     for k in range(n):
#         r,g,b = img.getpixel((x,y))
#         if (r < 100):
#             return 1
#         x += 1
#     return 0

# def jouer():
    
#     keyboard = Controller()
#     pos(759,207)
#     click()
#     pos(10,200)
#     to = temps()
#     keyboard.press(Key.down)
#     T = int((temps() - to))

#     TempsAttenteSaut = 0.01
#     TempsCoeff = 1.1
    
#     while ( Get()[0] < 1000 and T<90) :                            

#         T = int((temps() - to)*TempsCoeff)
       
#         x1 = 715 + T
#         x2 = 830 + T
#         L = x2-x1    
         
#         y1 = 311
#         y2 = 313               
#         H = y2 - y1         

#         img1 = ImageGrab.grab(bbox=(x1,y1,x2,y2))
        
#         Noir1 = TestPixMult(0,1,L,img1)

#         if ( Noir1 == 1 ):                   
#             keyboard.release(Key.down)
#             keyboard.press(Key.space)
#             time.sleep(TempsAttenteSaut)
#             img1 = ImageGrab.grab(bbox=(x1,y1,x2,y2))
#             while(TestPixMult(0,1,50,img1) == 1):
#                     img1 = ImageGrab.grab(bbox=(x1,y1,x2,y2))
                    
#         img1 = ImageGrab.grab(bbox=(630,311,700,313))
#         img2 = ImageGrab.grab(bbox=(700,311,780,313))
#         if (TestPixMult(0,1,70,img1) == 1 and TestPixMult(0,1,80,img2) == 0):
#                 keyboard.release(Key.space) 
#                 keyboard.press(Key.down)

                
# time.sleep(2)
# jouer()
