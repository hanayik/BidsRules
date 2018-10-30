#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.8.3 on Mon Oct 29 06:55:53 2018
#

import wx
import json
import sys
import os
from glob import glob
fullfile = os.path.join

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade

droppedFiles = []


QAfiles = glob('./json_qa/*.json')
print(QAfiles)

# get datatypes file path
datatypesFile = fullfile(os.path.dirname(__file__), 'datatypes.json')
print(datatypesFile)

# read in bids datatypes
with open(datatypesFile) as f:
    alldatatypes = json.load(f)

exampleCrit = ['crit 1', 'crit 2', 'crit 3']

def dealWithDroppedFiles(files):
    #print(files)
    droppedFiles = files
    print(droppedFiles)


class MyFileDropTarget(wx.FileDropTarget):
    """"""
    # filenames = []
    # ----------------------------------------------------------------------
    def __init__(self, window):
        """Constructor"""
        wx.FileDropTarget.__init__(self)
        self.window = window

    # ----------------------------------------------------------------------
    def OnDropFiles(self, x, y, filenames):
        dealWithDroppedFiles(filenames)
        return True



class MainWindow(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MainWindow.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)

        self.SetSize((720, 500))
        self.LabelPanel = wx.Panel(self, wx.ID_ANY, style=wx.BORDER_NONE)
        self.SeriesPanel = wx.ScrolledWindow(self, wx.ID_ANY, style=wx.BORDER_NONE)
        sizer_1 = wx.FlexGridSizer(2, 1, 2, 0)
        grid_sizer_1 = wx.FlexGridSizer(0, 4, 5, 0)
        grid_sizer_2 = wx.FlexGridSizer(0, 4, 0, 0)

        dt = MyFileDropTarget(self)

        self.SetDropTarget(dt)
        self.SetTitle("BIDS Rules")
        self.LabelPanel.SetMinSize((720, 30))
        self.SeriesPanel.SetScrollRate(10, 10)

        # seriesLabel = wx.StaticText(self.LabelPanel, wx.ID_ANY, "Series Name")
        # grid_sizer_2.Add(seriesLabel, 0, wx.LEFT | wx.RIGHT, 5)
        # datatypeLabel = wx.StaticText(self.LabelPanel, wx.ID_ANY, "BIDS Data type")
        # grid_sizer_2.Add(datatypeLabel, 0, wx.LEFT | wx.RIGHT, 5)
        # criteriaLabel = wx.StaticText(self.LabelPanel, wx.ID_ANY, "Rule criteria")
        # grid_sizer_2.Add(criteriaLabel, 0, wx.LEFT | wx.RIGHT, 5)
        # customLabel = wx.StaticText(self.LabelPanel, wx.ID_ANY, "Custom label")
        # grid_sizer_2.Add(customLabel, 0, wx.LEFT | wx.RIGHT, 5)
        self.LabelPanel.SetSizer(grid_sizer_2)
        sizer_1.Add(self.LabelPanel, 0, wx.EXPAND, 0)
        self.SeriesPanel.SetSizer(grid_sizer_1)
        sizer_1.Add(self.SeriesPanel, 0, wx.ALL | wx.EXPAND, 6)
        self.SetSizer(sizer_1)
        sizer_1.AddGrowableRow(1)
        self.Layout()
        
        for i, item in enumerate(QAfiles):
            if i == 0:
                seriesLabel = wx.StaticText(self.SeriesPanel, wx.ID_ANY, "Series Name")
                grid_sizer_1.Add(seriesLabel, 0, wx.LEFT | wx.RIGHT, 5)
                datatypeLabel = wx.StaticText(self.SeriesPanel, wx.ID_ANY, "BIDS Data type")
                grid_sizer_1.Add(datatypeLabel, 0, wx.LEFT | wx.RIGHT, 5)
                criteriaLabel = wx.StaticText(self.SeriesPanel, wx.ID_ANY, "Rule criteria")
                grid_sizer_1.Add(criteriaLabel, 0, wx.LEFT | wx.RIGHT, 5)
                customLabel = wx.StaticText(self.SeriesPanel, wx.ID_ANY, "Custom label")
                grid_sizer_1.Add(customLabel, 0, wx.LEFT | wx.RIGHT, 5)

            self.bidsDatatype = wx.Choice(self.SeriesPanel, wx.ID_ANY, choices=alldatatypes['datatypes'], name="bchoice"+str(i))
            self.bidsDatatype.SetToolTip(
                "anat:T1w T1-weighted image (fat is bright)\nanat:T2w T2-weighted image (water is bright)\nanat:T1rho Quantave T1rho brain imaging\nanat:T1map quantitative T1 map\nanat:T2map quantitative T2 map\nanat:T2star High resolution T2** image\nanat:FLAIR T2-FLAIR (pathology bright)\nanat:FLASH FLASH\nanat:PD Proton density\nanat:PDmap Proton density map\nanat:PDT2 Combined PD/T2\nanat:angio Angiography\nfunc:bold Functional imaging: T2star images used for task-based or rest ima\ndwi:dwi Diffusion weighted imaging\ndiscard Images with this data type will not be saved (e.g. localizer)\n")
            self.criteriaChooser = wx.Choice(self.SeriesPanel, wx.ID_ANY, choices=exampleCrit, name="cchoice"+str(i))
            self.customLabelTxt = wx.TextCtrl(self.SeriesPanel, wx.ID_ANY, "")
            seriesName = wx.StaticText(self.SeriesPanel, wx.ID_ANY, item)
            seriesName.SetToolTip("Series name from DICOM images")
            grid_sizer_1.Add(seriesName, 0, wx.LEFT | wx.RIGHT, 5)
            grid_sizer_1.Add(self.bidsDatatype, 0, wx.LEFT | wx.RIGHT, 5)
            grid_sizer_1.Add(self.criteriaChooser, 0, wx.LEFT | wx.RIGHT, 5)
            grid_sizer_1.Add(self.customLabelTxt, 0, wx.LEFT | wx.RIGHT, 5)
        # end wxGlade

# end of class MainWindow

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MainWindow(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
