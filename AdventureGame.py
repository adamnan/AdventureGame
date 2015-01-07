#! /usr/bin/env python
import wx

class MazeFrame(wx.Frame):

    def __init__(self, parent):

        wx.Frame.__init__(self, parent, wx.ID_ANY, "Our Title")

        self.panel = wx.Panel(self)

# ---------- Main Program Below ----------

app = wx.App(False)

initFrame = MazeFrame(None)

initFrame.Show()

app.MainLoop()
