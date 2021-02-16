#Import librairie
from tkinter import *
from time import *

#Import other function

class Pad:
    def __init__(self):
        self.Window = Tk()
        self.Windows_Width = 700
        self.Windows_Height = 300
        self.Nb_Button = 8
        self.Button_Height= 80
        self.Button_Width = 80
        self.Nb_line = 2
        self.All_Button = []
        self.Btn_X_List = []
        self.Btn_Y_List = []
        self.Time_0 = 0
        self.Time_Last = 0
        self.Time_Limit = 1
        self.btn_rec = 0
        self.Btn_State = [ False for k in range(0,self.Nb_Button)]
        self.Fond = Canvas(self.Window, width=self.Windows_Width+10, height=self.Windows_Height+10, bg='gray10')
        self.Command_List = [ "1","2","3","4","5","6","7","8" ]
        self.Color_Rec = [" ","red","white"]
        self.Rec_Color_Selecteur = 1
        self.USB = "../USB_to_pc.txt"
        self.Command_to_PAD = ""
        self.Create_PAD()
        self.Loop()
        self.Window.mainloop()
        
    def Create_PAD(self):
        self.Window.title("PAD Simulation ")
        self.Window.geometry("{0}x{1}+0+0".format(self.Windows_Width, self.Windows_Height))
        self.Fond.pack(padx=0,pady=0)
        self.Create_Button()
        self.Bouton_Quit()

    def Bouton_Quit(self):
        Btn_Quit = Button(self.Window, text ="Quitter", command = self.Window.destroy )
        Btn_Quit.place(x = 10, y = 10, height = 25, width = 75)

    def Create_Button(self):
        i = 0
        for Line in range(0,self.Nb_line) :
            for Column in range(0, int(self.Nb_Button/self.Nb_line) ) :
                i += 1
                self.Btn_Y_List.append( int ( int( self.Windows_Height / 3 ) * ( Line + 0.7 ) ) )
                self.Btn_X_List.append( int ( int( self.Windows_Width / (self.Nb_Button/self.Nb_line + 1) ) * ( Column + 0.8 ) ) )
                self.All_Button.append( Button(self.Window, text ="Button " + self.Command_List[i-1] , bg = "white" , command = lambda i = Line*4 + (Column + 1) : self.Update_Input(i) ) )
                self.All_Button[-1].place(x = self.Btn_X_List[-1] , y = self.Btn_Y_List[-1] , height = self.Button_Height , width = self.Button_Width )

    def Send_USB(self,commande):
        with open(self.USB, 'a') as USB_file :
            USB_file.write(commande + "\n")
        USB_file.close()

    def Update_Input(self,n):
        self.Time_Last = 0
        self.Btn_State[n-1] = not self.Btn_State[n-1]

        if not self.Btn_State[n-1] :
            self.Send_USB( "r" + str(n) )
            self.btn_rec = n

        if self.Btn_State[n-1] :
            if self.btn_rec == 0 :
                self.Color_Button(n,"red")
                self.Time_0 = time()
            else :
                self.Send_USB( "s" + str(n) )
                self.btn_rec = 0
                self.Btn_State[n-1] = not self.Btn_State[n-1]
                self.Color_Button(n,"white")

    def Color_Button(self,n,color):
        self.All_Button[n-1].destroy()
        self.All_Button[n-1] = Button(self.Window, text ="Button " + self.Command_List[n-1] , bg = color , command = lambda i = n : self.Update_Input(i) ) 
        self.All_Button[n-1].place(x = self.Btn_X_List[n-1] , y = self.Btn_Y_List[n-1] , height = self.Button_Height , width = self.Button_Width )

    def Loop(self):
        self.Command_to_PAD = ""
        
        self.Time_Last = int( time() - self.Time_0 )
        for n , State in enumerate(self.Btn_State) :
            if State and self.Time_Last > self.Time_Limit :
                self.Send_USB( "f" + str(n+1) )
                self.Btn_State[n] = not self.Btn_State[n]
                self.Color_Button(n + 1,"white")

        if self.btn_rec != 0 :
            self.Rec_Color_Selecteur = -self.Rec_Color_Selecteur
            self.Color_Button(self.btn_rec,self.Color_Rec[self.Rec_Color_Selecteur])

        if self.Command_to_PAD != "" :
            #Quand l'enreistrement est  est fini on etteint la lumiere

            #Quand le racourci est fini on etteint le lumiere
            print(Command_to_PAD)
            self.Command_to_PAD = ""

        self.Window.after( 500 , lambda: self.Loop() )

Pad()




        