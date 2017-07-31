import datetime
import wx


class sveglia(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="Sveglia", id=-1)
        self.frequenza = 99.4
        font = wx.Font(30, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)

        self.orologio = wx.StaticText(self, -1, label=(datetime.datetime.now().strftime("%A %d-%m-%y %H:%M:%S")))
        self.orologio.SetFont(font)

        self.lblfrequenza = wx.StaticText(self, -1, label=str(self.frequenza))
        self.lblfrequenza.SetFont(font)

        sizer = wx.GridSizer(1, 2, 5, 5)
        sizer.Add(self.orologio, 0, wx.ALL | wx.CENTRE | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTRE_VERTICAL)
        sizer.Add(self.lblfrequenza, 1, wx.ALL | wx.CENTRE | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTRE_VERTICAL)
        self.SetSizer(sizer)

        self.update()
        self.Fit()

        self.Bind(wx.EVT_KEY_DOWN, self.onKey)
        self.Bind(wx.EVT_KEY_DOWN, self.cambiaVolume)
        self.ShowFullScreen(True)

    def cambiaVolume(self, evt):
        keyCode = evt.GetKeyCode()
        # print(keyCode)
        if keyCode == 43:
            self.frequenza += 0.1
            self.lblfrequenza.SetLabel("{0:0.1f}".format(self.frequenza))
        elif keyCode == 45:
            self.frequenza -= 0.1
            self.lblfrequenza.SetLabel("{0:0.1f}".format(self.frequenza))
        else:
            evt.Skip()

    def onKey(self, evt):
        key_code = evt.GetKeyCode()
        if key_code == wx.WXK_ESCAPE:
            self.Destroy()
        else:
            evt.Skip()

    def update(self):
        current_time = datetime.datetime.strftime(datetime.datetime.now(), '%A %d-%m-%Y %H:%M:%S')
        self.orologio.SetLabel(current_time)
        wx.CallLater(1000, self.update)

app = wx.App(False)
base = sveglia()
base.Show()
app.MainLoop()
