#Import librairie
from tkinter import *

#Import other function


class Pad:
    def __init__(self):
        self.Window = Tk()
        self.Windows_Width = 700
        self.Windows_Height = 300

        self.Nb_Button = 8
        self.Button_Height= 60
        self.Button_Width = 60
        self.Nb_line = 2
        
        self.All_Button = []
        self.Fond = Canvas(self.Window, width=self.Windows_Width+10, height=self.Windows_Height+10, bg='gray10')

        self.Command_List = [ ["1","2","3","4"],["5","6","7","8"] ]

        self.Create_PAD()
        self.Window.mainloop()
        
    def Create_PAD(self):
        self.Window.title("PAD Simulation ")

        self.Window.geometry("{0}x{1}+0+0".format(self.Windows_Width, self.Windows_Height))
        self.Fond.pack(padx=0,pady=0)

        self.Create_Button()

        self.Bouton_Quit()

    def Screen_Destroy(self):
        for Element in self.Widget :
            Element.destroy()

    def Create_Button(self):
        i = 0
        for Line in range(0,self.Nb_line) :
            y = int ( int( self.Windows_Height / 3 ) * ( Line + 0.7 ) )
            for Column in range(0, int(self.Nb_Button/self.Nb_line) ) :
                x = int ( int( self.Windows_Width / (self.Nb_Button/self.Nb_line + 1) ) * ( Column + 0.8 ) )
                i += 1
                self.All_Button.append( Button(self.Window, text ="Button " + self.Command_List[Line][Column] , command = lambda i = Line*4 + (Column + 1) : self.Send_USB(i) ) )
                self.All_Button[-1].place(x = x , y = y , height = self.Button_Height , width = self.Button_Width )
                print(Line,Column,self.Command_List[Line][Column])

    def Bouton_Quit(self):
        Btn_Quit = Button(self.Window, text ="Quitter", command = self.Window.destroy )
        Btn_Quit.place(x = 10, y = 10, height = 25, width = 75)

    def Send_USB(self,i):
        print(i)

Pad = Pad()
Pad.Window.mainloop()


        