#! /usr/bin/env python
import wx

class MazeFrame(wx.Frame):

    def __init__(self, parent):

        wx.Frame.__init__(self, parent, wx.ID_ANY, "Maze Runner", size=(864,510))

        self.initPictureFile = wx.Image("1.png", wx.BITMAP_TYPE_ANY)

        self.initPictureBitmap = self.initPictureFile.ConvertToBitmap()

        self.initPicture = wx.StaticBitmap(self, wx.ID_ANY, self.initPictureBitmap, pos=(5,5))

        self.panel = wx.Panel(self)

# ---------- Main Program Below ----------

app = wx.App(False)

initFrame = MazeFrame(None)

initFrame.Show()

app.MainLoop()
