#! /usr/bin/env python
import wx

class Frame1(wx.Frame):

	def __init__(self, parent):
	
		wx.Frame.__init__(self, parent, wx.ID_ANY, "Maze Runner", pos=(150, 200), size=(864,510))
		self.initPictureFile = wx.Image("1.png", wx.BITMAP_TYPE_ANY)
		self.initPictureBitmap = self.initPictureFile.ConvertToBitmap()
		self.initPicture = wx.StaticBitmap(self, wx.ID_ANY, self.initPictureBitmap, pos=(5,5))
		self.panel = wx.Panel(self)
		
		btn = wx.Button(self, label="Start Game", pos=(357,350), size=(150,50))
		btn.Bind(wx.EVT_BUTTON, self.OnBtn)
		
	def OnBtn(self, e):
		self.Hide()
		secondWindow = Frame2(self)
		secondWindow.Show()
		
class Frame2(wx.Frame):

	def __init__(self, parent):

		wx.Frame.__init__(self, parent, wx.ID_ANY, "Inferno", pos=(150, 200), size=(864,510))
		self.turnPictureFile = wx.Image("2.png", wx.BITMAP_TYPE_ANY)
		self.turnPictureBitmap = self.turnPictureFile.ConvertToBitmap()
		self.turnPicture = wx.StaticBitmap(self, wx.ID_ANY, self.turnPictureBitmap, pos=(5,5))
		self.panel = wx.Panel(self)
		
		btn1 = wx.Button(self, label="Go Left", pos=(273,200), size=(70,50))
		btn1.Bind(wx.EVT_BUTTON, self.OnBtn1)
		
		btn2 = wx.Button(self, label="Go Right", pos=(427,200), size=(70,50))
		btn2.Bind(wx.EVT_BUTTON, self.OnBtn2)

	def OnBtn1(self, e):
		self.Hide()
		secondWindow = Frame3(self)
		secondWindow.Show()
		
	def OnBtn2(self, e):
		self.Hide()
		secondWindow = Frame4(self)
		secondWindow.Show()

class Frame3(wx.Frame):

	def __init__(self, parent):

		wx.Frame.__init__(self, parent, wx.ID_ANY, "Void", pos=(150, 200), size=(864,510))
		self.dilemmaLFile = wx.Image("3.png", wx.BITMAP_TYPE_ANY)
		self.dilemmaLBitmap = self.dilemmaLFile.ConvertToBitmap()
		self.dilemmaL = wx.StaticBitmap(self, wx.ID_ANY, self.dilemmaLBitmap, pos=(5,5))
		self.panel = wx.Panel(self)
		
		btn3 = wx.Button(self, label="Go Left", pos=(273,200), size=(70,50))
		btn3.Bind(wx.EVT_BUTTON, self.OnBtn3)
		
		btn4 = wx.Button(self, label="Go Right", pos=(427,200), size=(70,50))
		btn4.Bind(wx.EVT_BUTTON, self.OnBtn4)
		
	def OnBtn3(self,e):
		self.Hide()
		secondWindow = Frame1(self)
		secondWindow.Show()
		
	def OnBtn4(self, e):
		self.Hide()
		secondWindow = Frame6(self)
		secondWindow.Show()
		
class Frame4(wx.Frame):

	def __init__(self, parent):

		wx.Frame.__init__(self, parent, wx.ID_ANY, "Twilight", pos=(150, 200), size=(864,510))
		self.dilemmaRFile = wx.Image("4.png", wx.BITMAP_TYPE_ANY)
		self.dilemmaRBitmap = self.dilemmaRFile.ConvertToBitmap()
		self.dilemmaR = wx.StaticBitmap(self, wx.ID_ANY, self.dilemmaRBitmap, pos=(5,5))
		self.panel = wx.Panel(self)
		
		btn5 = wx.Button(self, label="Go Left", pos=(273,200), size=(70,50))
		btn5.Bind(wx.EVT_BUTTON, self.OnBtn5)
		
		btn6 = wx.Button(self, label="Go Right", pos=(427,200), size=(70,50))
		btn6.Bind(wx.EVT_BUTTON, self.OnBtn6)
		
	def OnBtn5(self,e):
		self.Hide()
		secondWindow = Frame5(self)
		secondWindow.Show()
		
	def OnBtn6(self, e):
		self.Hide()
		secondWindow = Frame1(self)
		secondWindow.Show()
		
class Frame5(wx.Frame):

	def __init__(self, parent):

		wx.Frame.__init__(self, parent, wx.ID_ANY, "Maze Runner", pos=(150, 200), size=(864,510))
		self.keyFile = wx.Image("5.png", wx.BITMAP_TYPE_ANY)
		self.keyBitmap = self.keyFile.ConvertToBitmap()
		self.key = wx.StaticBitmap(self, wx.ID_ANY, self.keyBitmap, pos=(5,5))
		self.panel = wx.Panel(self)
		
		btn = wx.Button(self, label="Open it", pos=(357,350), size=(150,50))
		btn.Bind(wx.EVT_BUTTON, self.OnBtn)
		
	def OnBtn(self, e):
		self.Hide()
		secondWindow = Frame7(self)
		secondWindow.Show()
		Frame6.Show(False)
		Frame7.Show(True)
		
class Frame6(wx.Frame):

	def __init__(self, parent):
	
		wx.Frame.__init__(self, parent, wx.ID_ANY, "Abyss", pos=(150, 200), size=(864,510))
		self.darkFile = wx.Image("6.png", wx.BITMAP_TYPE_ANY)
		self.darkBitmap = self.darkFile.ConvertToBitmap()
		self.dark = wx.StaticBitmap(self, wx.ID_ANY, self.darkBitmap, pos=(5,5))
		self.panel = wx.Panel(self)
		
		btn = wx.Button(self, label="Back to Inferno", pos=(357,250), size=(150,50))
		btn.Bind(wx.EVT_BUTTON, self.OnBtn)
		
	def OnBtn(self, e):
		self.Hide()
		secondWindow = Frame2(self)
		secondWindow.Show()
		
class Frame7(wx.Frame):

	def __init__(self, parent):
	
		wx.Frame.__init__(self, parent, wx.ID_ANY, "Abyss", pos=(150, 200), size=(864,510))
		self.lightFile = wx.Image("7.png", wx.BITMAP_TYPE_ANY)
		self.lightBitmap = self.lightFile.ConvertToBitmap()
		self.light = wx.StaticBitmap(self, wx.ID_ANY, self.lightBitmap, pos=(5,5))
		self.panel = wx.Panel(self)
		
		btn = wx.Button(self, label="Hope is there", pos=(357,250), size=(150,50))
		btn.Bind(wx.EVT_BUTTON, self.OnBtn)
		
	def OnBtn(self, e):
		self.Hide()
		secondWindow = Frame2(self)
		secondWindow.Show()
		
class Frame8(wx.Frame):
		

# ---------- Main Program Below ----------

app = wx.App(False)

initFrame = Frame1(None)

initFrame.Show()

app.MainLoop()
