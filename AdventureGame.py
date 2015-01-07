#! /usr/bin/env python
import wx

class Frame1(wx.Frame):

	def __init__(self, parent):
	
		wx.Frame.__init__(self, parent, wx.ID_ANY, "Maze Runner", pos=(150, 200), size=(864,510))
		self.initPictureFile = wx.Image("1.png", wx.BITMAP_TYPE_ANY)
		self.initPictureBitmap = self.initPictureFile.ConvertToBitmap()
		self.initPicture = wx.StaticBitmap(self, wx.ID_ANY, self.initPictureBitmap, pos=(5,5))
		self.panel = wx.Panel(self)
		self.btnstart = wx.Button(self.panel, label="Switch", pos=(1, 1))
		self.btnstart.Bind(wx.EVT_BUTTON, self.Switch)
		
	def Switch(self, e):
	
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
		
class Frame3(wx.Frame):

	def __init__(self, parent):
	
		wx.Frame.__init__(self, parent, wx.ID_ANY, "Maze Runnuer", pos=(150, 200), size=(864,510))

# ---------- Main Program Below ----------

app = wx.App(False)

initFrame = Frame1(None)

initFrame.Show()

app.MainLoop()
