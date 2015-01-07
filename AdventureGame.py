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

		wx.Frame.__init__(self, parent, wx.ID_ANY, "Maze Runner", pos=(150, 200), size=(864,510))
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

		wx.Frame.__init__(self, parent, wx.ID_ANY, "Maze Runner", pos=(150, 200), size=(864,510))
		
class Frame4(wx.Frame):

	def __init__(self, parent):

		wx.Frame.__init__(self, parent, wx.ID_ANY, "Maze Runner", pos=(150, 200), size=(864,510))


# ---------- Main Program Below ----------

app = wx.App(False)

initFrame = Frame1(None)

initFrame.Show()

app.MainLoop()
