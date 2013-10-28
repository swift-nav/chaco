""" Unit test to make sure our example for embedding a Chaco plot in a WX app
works.

Source: http://docs.enthought.com/chaco/user_manual/how_do_i.html
"""
import os
os.environ["ETS_TOOLKIT"]="wx"
import wx
from numpy import arange
from scipy.special import jn
from chaco.api import HPlotContainer, create_line_plot
from enable.api import Window

import unittest

class PlotFrame(wx.Frame):
    def __init__(self, *args, **kw):
        kw["size"] = (850, 550)
        wx.Frame.__init__( *(self,) + args, **kw )
        self.plot_window = Window(self, component=self._create_plot())
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.plot_window.control, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.SetAutoLayout(True)
        self.Show(True)
        return

    def _create_plot(self):
        x = arange(-5.0, 15.0, 20.0/100)
        y = jn(0, x)
        plot = create_line_plot((x,y), bgcolor="white",
                                    add_grid=True, add_axis=True)
        container = HPlotContainer(spacing=20, padding=50, bgcolor="lightgray")
        container.add(plot)
        return container


class TestWxApp(unittest.TestCase):

    def test_building_app(self):
        app = wx.PySimpleApp()
        frame = PlotFrame(None)
        # Programmatically destroy the application and frame instead of
        # starting the GUI event loop like in the example.
        frame.Close()
        app.Destroy()
