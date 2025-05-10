import wx
import datetime


class DateTimeLabel(wx.StaticText):
    def __init__(self, parent):
        super().__init__(parent, label=self.get_formatted_time())
        # Set font
        font = self.GetFont()
        font.PointSize = 18
        font.SetWeight(wx.FONTWEIGHT_BOLD)
        self.SetFont(font)
        # Refresh Timer
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.update_time, self.timer)
        self.timer.Start(1000)


    def get_formatted_time(self):
        now = datetime.datetime.now()
        return now.strftime("%A | %#m/%#d/%Y | %#I:%M %p")


    def update_time(self, event):
        self.SetLabel(self.get_formatted_time())


class App(wx.App):
    def OnInit(self):
        self.frame = wx.Frame(parent=None, title="Formatted DateTime", size=(800, 600))
        panel = wx.Panel(self.frame)
        sizer = wx.FlexGridSizer(rows=2, cols=2, hgap=10, vgap=10)
        # row 0, col 0
        self.datetime_label = DateTimeLabel(panel)
        sizer.Add(self.datetime_label, 0, wx.EXPAND)
        # row 0, col 1
        sizer.Add(wx.Button(panel, label="Admin"), 0, wx.ALIGN_CENTER)
        # row 1, col 0
        sizer.Add(wx.Button(panel, label="Bottom Left"), 0, wx.EXPAND)
        # row 1, col 1
        sizer.Add(wx.Button(panel, label="Bottom Right"), 0, wx.EXPAND)
        # Grow Rows / Columns
        sizer.AddGrowableRow(1)
        sizer.AddGrowableCol(0)
        sizer.AddGrowableCol(1)
        # Assign
        panel.SetSizer(sizer)
        self.frame.Show()
        return True


if __name__ == "__main__":
    app = App()
    app.MainLoop()
