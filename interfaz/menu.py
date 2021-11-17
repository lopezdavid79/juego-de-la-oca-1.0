import wx

class Menu(wx.Frame):
    def __init__(self, parent  , *args , **qwargs):
        super().__init__(parent , *args ,** qwargs )
        self.menu()
    def menu(self):
        menubar=wx.MenuBar()
        file_menu = wx.Menu()
        jugar = file_menu.Append(-1 , 'jugar')
        salir = file_menu.Append(-1 , 'salir')
        menubar.Append(file_menu, '&Menu')
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.jugar, jugar)
        self.Bind(wx.EVT_MENU, self.OnQuit, salir)
        self.SetTitle('Juego de la Oca')
        self.Show()

    def jugar(self ,event):
        print('hora de jugar')






    def OnQuit(self , event):
        self.Close()