#Import librairie
import time 
from ctypes import *
import ctypes
from pynput.keyboard import Key, Controller
import os

#Import other function
from Macro import *

def Add_Line(file,text):
    with open(file, 'a') as file :
            file.write(text + "\n")
    file.close()

class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]

def Pointer_Pos():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return([pt.x,pt.y])

def Write_click(Maccro_Data_File,data):
    Position = Pointer_Pos()
    Add_Line(Maccro_Data_File,data + "_" + str(Position[0]) + "_" + str(Position[1]) )

def Detect_click(event):
    Left = 0x01
    Right = 0x02
    if ctypes.windll.user32.GetKeyState(Left) > 200 and not event[0][1] :
        event[0] = [True,True]
    if ctypes.windll.user32.GetKeyState(Left) < 200 and event[0][1] :
        event[0] = [True,False]
    if ctypes.windll.user32.GetKeyState(Right) > 200 and not event[1][1] :
        event[1] = [True,True]
    if ctypes.windll.user32.GetKeyState(Right) < 200 and event[1][1] :
        event[1] = [True,False]
    return event

def Execute_Macros(Button,file):
    print("Execution maccro " + str(Button) )
    Maccro_Data_File = file + str(Button) +".txt"
    with open(Maccro_Data_File, 'r') as Maccro :
            line = Maccro.readlines()[0:-2]
            for Actions in line :
                time.sleep(1)
                Data_Action = Actions.split("_")
                x = int(Data_Action[2])
                y = int(Data_Action[3])
                ctypes.windll.user32.SetCursorPos(x, y)
                if Data_Action[0] == "L" :
                    if Data_Action[1] == "1" :
                        ctypes.windll.user32.mouse_event(2, 0, 0, 0,0)
                    elif Data_Action[1] == "0" :
                        ctypes.windll.user32.mouse_event(4, 0, 0, 0,0)

def Record_Macros(USB,Button,Maccro_Data_File):
    Maccro_Data_File = Maccro_Data_File + str(Button) +".txt"
    Command_to_pc = " "
    Maccro = open(Maccro_Data_File ,'w')
    Maccro.close()
    #         change state change state
    Event = [[False,False],[False,False]]
    while  Command_to_pc[0] != "s" :
        with open(USB, 'r') as USB_file :
            Command_to_pc = USB_file.readlines()
            Command_to_pc = Command_to_pc[-1]
        USB_file.close() 
        Event = Detect_click(Event)
        if Event[1][0] :
            if Event[1][1] :
                Click = "R_1"
            else :
                Click = "R_0"
            Event[1][0] = False
            Write_click(Maccro_Data_File,Click)

        if Event[0][0] :
            if Event[0][1] :
                Click = "L_1"
            else :
                Click = "L_0"
            Event[0][0] = False
            Write_click(Maccro_Data_File,Click)

    
    print("Stop Record maccro " + str(Button) )

def Link():
    Maccro_Data_File = "Macros_Data/Maccro_"
    Sim = True #input("Do you want to simulate the PAD : ")
    if Sim :
        USB = "../USB_to_pc.txt"
        Command_to_pc = ""
    else : 
        print("Checking USB...")
        print("No pad detected")
    
    Running = True
    while Running :
        time.sleep(0.5)
        with open(USB, 'r') as USB_file :
            Command_to_pc = USB_file.readlines()
            Command_to_pc = Command_to_pc[-1]
        USB_file.close()

        if Command_to_pc[0] != "D" :
            if Command_to_pc[0] == "f" :
                Execute_Macros(Command_to_pc[1],Maccro_Data_File)
            
            elif Command_to_pc[0] == "r" :
                Record_Macros(USB,Command_to_pc[1],Maccro_Data_File)
               
            with open(USB, 'a') as USB_file :
                USB_file.write("D" + "\n")
            USB_file.close()

Link()
        