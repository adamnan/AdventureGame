#! /usr/bin/env python
import wx

class Frame1(wx.Frame):

	check = 0

	def __init__(self, parent):
	
		wx.Frame.__init__(self, parent, wx.ID_ANY, "Maze Runner", pos=(150, 200), size=(864,510))
				
		self.panel1 = wx.Panel(self, size=(864,510))
		
		self.initPictureFile = wx.Image("1.png", wx.BITMAP_TYPE_ANY)
		self.initPictureBitmap = self.initPictureFile.ConvertToBitmap()
		self.initPicture = wx.StaticBitmap(self.panel1, wx.ID_ANY, self.initPictureBitmap, pos=(5,5))
		
		text = wx.StaticText(self.panel1, label = "ABANDON HOPE, ALL YE WHO ENTER HERE.", pos = (289, 100))
		text.SetForegroundColour((255,255,255))
		text.SetBackgroundColour((0,0,0))
		
		btn = wx.Button(self.panel1, label="Start Game", pos=(357,350), size=(150,50))
		btn.Bind(wx.EVT_BUTTON, self.OnBtn)

		
		self.panel2 = wx.Panel(self, size=(864,510))		
		
		self.turnPictureFile = wx.Image("2.png", wx.BITMAP_TYPE_ANY)
		self.turnPictureBitmap = self.turnPictureFile.ConvertToBitmap()
		self.turnPicture = wx.StaticBitmap(self.panel2, wx.ID_ANY, self.turnPictureBitmap, pos=(5,5))
		
		text = wx.StaticText(self.panel2, label = "YOU ARE LEADED TO INFERNO, LEFT HOPE HERE ONCE.", pos = (210, 100))
		text.SetForegroundColour((255,255,255))
		text.SetBackgroundColour((0,0,0))
		
		text = wx.StaticText(self.panel2, label = "Left...?", pos = (289, 150))
		text.SetForegroundColour((255,255,255))
		text.SetBackgroundColour((0,0,0))
		
		btn1 = wx.Button(self.panel2, label="Go Left", pos=(273,200), size=(70,50))
		btn1.Bind(wx.EVT_BUTTON, self.OnBtn1)
		
		btn2 = wx.Button(self.panel2, label="Go Right", pos=(427,200), size=(70,50))
		btn2.Bind(wx.EVT_BUTTON, self.OnBtn2)

		
		self.panel3 = wx.Panel(self, size=(864,510))
		
		self.dilemmaLFile = wx.Image("3.png", wx.BITMAP_TYPE_ANY)
		self.dilemmaLBitmap = self.dilemmaLFile.ConvertToBitmap()
		self.dilemmaL = wx.StaticBitmap(self.panel3, wx.ID_ANY, self.dilemmaLBitmap, pos=(5,5))
		
		text = wx.StaticText(self.panel3, label = "THE DARKEST TIME IS WHEN YOU ARE TRAPPED INTO A DILEMMA... VOID IS COMING...", pos = (160, 100))
		text.SetForegroundColour((255,255,255))
		text.SetBackgroundColour((0,0,0))
		
		btn3 = wx.Button(self.panel3, label="Go Left", pos=(303,200), size=(70,50))
		btn3.Bind(wx.EVT_BUTTON, self.OnBtn3)
		
		btn4 = wx.Button(self.panel3, label="Go Right", pos=(517,200), size=(70,50))
		btn4.Bind(wx.EVT_BUTTON, self.OnBtn4)

		
		self.panel4 = wx.Panel(self, size=(864,510))

		self.dilemmaRFile = wx.Image("4.png", wx.BITMAP_TYPE_ANY)
		self.dilemmaRBitmap = self.dilemmaRFile.ConvertToBitmap()
		self.dilemmaR = wx.StaticBitmap(self.panel4, wx.ID_ANY, self.dilemmaRBitmap, pos=(5,5))

		text = wx.StaticText(self.panel4, label = "CHUCKLE, CHUCKLE...PANDORA IS LEADING...", pos = (250, 100))
		text.SetForegroundColour((255,255,255))
		text.SetBackgroundColour((0,0,0))
		
		text = wx.StaticText(self.panel4, label = "\"Is there any box?\"", pos = (350, 150))
		text.SetForegroundColour((255,255,255))
		text.SetBackgroundColour((0,0,0))

		btn5 = wx.Button(self.panel4, label="Go Left", pos=(273,200), size=(70,50))
		btn5.Bind(wx.EVT_BUTTON, self.OnBtn5)
		
		btn6 = wx.Button(self.panel4, label="Go Right", pos=(457,200), size=(70,50))
		btn6.Bind(wx.EVT_BUTTON, self.OnBtn6)
		
		
		self.panel5 = wx.Panel(self, size=(864,510))

		self.keyFile = wx.Image("5.png", wx.BITMAP_TYPE_ANY)
		self.keyBitmap = self.keyFile.ConvertToBitmap()
		self.key = wx.StaticBitmap(self.panel5, wx.ID_ANY, self.keyBitmap, pos=(5,5))
		
		text = wx.StaticText(self.panel5, label = "A box!!!", pos = (160, 100))
		text.SetForegroundColour((255,255,255))
		text.SetBackgroundColour((0,0,0))
		
		btn7 = wx.Button(self.panel5, label="Open it", pos=(327,350), size=(150,50))
		btn7.Bind(wx.EVT_BUTTON, self.OnBtn7)
		
		
		self.panel6 = wx.Panel(self, size=(864,510))
				
		self.keyFile = wx.Image("6.png", wx.BITMAP_TYPE_ANY)
		self.keyBitmap = self.keyFile.ConvertToBitmap()
		self.key = wx.StaticBitmap(self.panel6, wx.ID_ANY, self.keyBitmap, pos=(5,5))
		
		text = wx.StaticText(self.panel6, label = "PRESENT...PRESENT, PAST, TOMORROW", pos = (160, 100))
		text.SetForegroundColour((255,255,255))
		text.SetBackgroundColour((0,0,0))
		
		text = wx.StaticText(self.panel6, label = "Do I need a present...?", pos = (200, 150))
		text.SetForegroundColour((255,255,255))
		text.SetBackgroundColour((0,0,0))
		
		btn8 = wx.Button(self.panel6, label="Back", pos=(357,350), size=(150,50))
		btn8.Bind(wx.EVT_BUTTON, self.OnBtn8)
		
		
		self.panel7 = wx.Panel(self, size=(864,510))
		
		self.keyFile = wx.Image("1.png", wx.BITMAP_TYPE_ANY)
		self.keyBitmap = self.keyFile.ConvertToBitmap()
		self.key = wx.StaticBitmap(self.panel7, wx.ID_ANY, self.keyBitmap, pos=(5,5))
		
		btn9 = wx.Button(self.panel7, label="Go on", pos=(357,350), size=(150,50))
		btn9.Bind(wx.EVT_BUTTON, self.OnBtn9)
		
		
		self.panelDeath = wx.Panel(self, size=(864,510))
		
		self.deathFile = wx.Image("death.png", wx.BITMAP_TYPE_ANY)
		self.deathBitmap = self.deathFile.ConvertToBitmap()
		self.death = wx.StaticBitmap(self.panelDeath, wx.ID_ANY, self.deathBitmap, pos=(5,5))
		
		btnDeath = wx.Button(self.panelDeath, label="Respawn", pos=(357,350), size=(150,50)
		btnDeath.Bind(wx.EVT_BUTTON, self.OnBtnDeath)
					
		self.panel2.Hide()
		self.panel3.Hide()
		self.panel4.Hide()
		self.panel5.Hide()
		self.panel6.Hide()
		self.panel7.Hide()
		self.panelDeath.Hide()
		
	def OnBtn(self, e):
		self.panel1.Hide()
		self.panel2.Show()
	
	def OnBtn1(self, e):
		self.panel2.Hide()
		self.panel3.Show()
		
	def OnBtn2(self, e):
		self.panel2.Hide()
		self.panel4.Show()
	
	def OnBtn3(self,e):
		self.panel3.Hide()
		self.panelDeath.Show()
		
	def OnBtn4(self, e):
		if self.check == 0:
			self.panel3.Hide()
			self.panel6.Show()
		elif self.check == 1:
			self.panel3.Hide()
			self.panel7.Show()
	
	def OnBtn5(self,e):
		self.panel4.Hide()
		self.panel5.Show()
		
	def OnBtn6(self, e):
		self.panel4.Hide()
		self.panelDeath.Show()
	
	def OnBtn7(self, e):
		self.panel5.Hide()
		self.panel2.Show()
		self.check = 1
		
	def OnBtn8(self, e):
		self.panel6.Hide()
		self.panel2.Show()
		
	def OnBtn9(self, e):
		self.panel7.Hide()
		self.panel8.Show()
		
	def OnBtnDeath(self, e):
		self.panel2.Show()		

# ---------- Main Program Below ----------

app = wx.App(False)

initFrame = Frame1(None)

initFrame.Show()

app.MainLoop()
