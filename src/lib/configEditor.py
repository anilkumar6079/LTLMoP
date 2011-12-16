#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Fri Dec 16 03:13:38 2011

import wx

# begin wxGlade: extracode
# end wxGlade



class simSetupDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: simSetupDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER|wx.THICK_FRAME
        wx.Dialog.__init__(self, *args, **kwds)
        self.sizer_22_staticbox = wx.StaticBox(self, -1, "Initial Conditions")
        self.sizer_1_staticbox = wx.StaticBox(self, -1, "Execution Environment")
        self.sizer_27_staticbox = wx.StaticBox(self, -1, "Experiment Settings")
        self.sizer_28_staticbox = wx.StaticBox(self, -1, "Experiment Configurations:")
        self.list_box_experiment_name = wx.ListBox(self, -1, choices=[])
        self.button_cfg_new = wx.Button(self, wx.ID_NEW, "")
        self.button_cfg_import = wx.Button(self, -1, "Import...")
        self.button_cfg_delete = wx.Button(self, wx.ID_DELETE, "")
        self.label_9 = wx.StaticText(self, -1, "Experiment Name: ")
        self.text_ctrl_sim_experiment_name = wx.TextCtrl(self, -1, "")
        self.label_2 = wx.StaticText(self, -1, "Custom Propositions:")
        self.list_box_init_customs = wx.CheckListBox(self, -1, choices=["1", "2"])
        self.label_2_copy = wx.StaticText(self, -1, "Action Propositions:")
        self.list_box_init_actions = wx.CheckListBox(self, -1, choices=["3", "4"])
        self.label_1 = wx.StaticText(self, -1, "Robots:")
        self.list_box_robots = wx.ListBox(self, -1, choices=[])
        self.button_addrobot = wx.Button(self, -1, "Add robot...")
        self.button_2 = wx.Button(self, -1, "Configure robot...")
        self.button_3 = wx.Button(self, -1, "Remove robot")
        self.button_4 = wx.Button(self, -1, "Edit proposition mapping...")
        self.button_sim_apply = wx.Button(self, wx.ID_APPLY, "")
        self.button_sim_ok = wx.Button(self, wx.ID_OK, "")
        self.button_sim_cancel = wx.Button(self, wx.ID_CANCEL, "")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_LISTBOX, self.onSimLoad, self.list_box_experiment_name)
        self.Bind(wx.EVT_BUTTON, self.onConfigNew, self.button_cfg_new)
        self.Bind(wx.EVT_BUTTON, self.onConfigImport, self.button_cfg_import)
        self.Bind(wx.EVT_BUTTON, self.onConfigDelete, self.button_cfg_delete)
        self.Bind(wx.EVT_TEXT, self.onSimNameEdit, self.text_ctrl_sim_experiment_name)
        self.Bind(wx.EVT_BUTTON, self.onClickAddRobot, self.button_addrobot)
        self.Bind(wx.EVT_BUTTON, self.onClickConfigureRobot, self.button_2)
        self.Bind(wx.EVT_BUTTON, self.onClickRemoveRobot, self.button_3)
        self.Bind(wx.EVT_BUTTON, self.onClickEditMapping, self.button_4)
        self.Bind(wx.EVT_BUTTON, self.onClickApply, self.button_sim_apply)
        self.Bind(wx.EVT_BUTTON, self.onClickOK, self.button_sim_ok)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: simSetupDialog.__set_properties
        self.SetTitle("Configure Execution")
        self.SetSize((935, 508))
        self.text_ctrl_sim_experiment_name.SetMinSize((300, 27))
        self.list_box_init_customs.SetSelection(0)
        self.list_box_init_actions.SetSelection(0)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: simSetupDialog.__do_layout
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_12 = wx.BoxSizer(wx.VERTICAL)
        sizer_13 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_27 = wx.StaticBoxSizer(self.sizer_27_staticbox, wx.VERTICAL)
        sizer_1 = wx.StaticBoxSizer(self.sizer_1_staticbox, wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_22 = wx.StaticBoxSizer(self.sizer_22_staticbox, wx.VERTICAL)
        sizer_23 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_17_copy = wx.BoxSizer(wx.VERTICAL)
        sizer_17 = wx.BoxSizer(wx.VERTICAL)
        sizer_30 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_29 = wx.BoxSizer(wx.VERTICAL)
        sizer_28 = wx.StaticBoxSizer(self.sizer_28_staticbox, wx.VERTICAL)
        sizer_29_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6.Add((20, 20), 0, 0, 0)
        sizer_29.Add((20, 20), 0, 0, 0)
        sizer_28.Add((20, 10), 0, 0, 0)
        sizer_28.Add(self.list_box_experiment_name, 1, wx.EXPAND, 0)
        sizer_28.Add((20, 20), 0, 0, 0)
        sizer_29_copy.Add(self.button_cfg_new, 0, 0, 0)
        sizer_29_copy.Add((10, 20), 0, 0, 0)
        sizer_29_copy.Add(self.button_cfg_import, 0, 0, 0)
        sizer_29_copy.Add((10, 20), 0, 0, 0)
        sizer_29_copy.Add(self.button_cfg_delete, 0, 0, 0)
        sizer_28.Add(sizer_29_copy, 0, wx.EXPAND, 0)
        sizer_28.Add((20, 10), 0, 0, 0)
        sizer_29.Add(sizer_28, 1, wx.EXPAND, 0)
        sizer_6.Add(sizer_29, 1, wx.EXPAND, 0)
        sizer_6.Add((20, 20), 0, 0, 0)
        sizer_12.Add((20, 20), 0, 0, 0)
        sizer_30.Add(self.label_9, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_30.Add((20, 20), 0, 0, 0)
        sizer_30.Add(self.text_ctrl_sim_experiment_name, 0, 0, 0)
        sizer_12.Add(sizer_30, 0, wx.EXPAND, 0)
        sizer_12.Add((20, 20), 0, 0, 0)
        sizer_23.Add((5, 20), 0, 0, 0)
        sizer_17.Add(self.label_2, 0, 0, 0)
        sizer_17.Add(self.list_box_init_customs, 1, wx.EXPAND, 0)
        sizer_23.Add(sizer_17, 1, wx.EXPAND, 0)
        sizer_23.Add((20, 20), 0, 0, 0)
        sizer_17_copy.Add(self.label_2_copy, 0, 0, 0)
        sizer_17_copy.Add(self.list_box_init_actions, 1, wx.EXPAND, 0)
        sizer_23.Add(sizer_17_copy, 1, wx.EXPAND, 0)
        sizer_23.Add((5, 20), 0, 0, 0)
        sizer_22.Add(sizer_23, 5, wx.EXPAND, 0)
        sizer_27.Add(sizer_22, 1, wx.ALL|wx.EXPAND, 10)
        sizer_3.Add(self.label_1, 0, 0, 0)
        sizer_3.Add(self.list_box_robots, 1, wx.EXPAND, 0)
        sizer_2.Add(sizer_3, 1, wx.EXPAND, 0)
        sizer_2.Add((20, 20), 0, 0, 0)
        sizer_4.Add(self.button_addrobot, 0, wx.BOTTOM, 5)
        sizer_4.Add(self.button_2, 0, wx.BOTTOM, 5)
        sizer_4.Add(self.button_3, 0, 0, 0)
        sizer_4.Add((20, 60), 0, 0, 0)
        sizer_4.Add(self.button_4, 0, 0, 0)
        sizer_2.Add(sizer_4, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
        sizer_27.Add(sizer_1, 0, wx.ALL|wx.EXPAND, 10)
        sizer_12.Add(sizer_27, 1, wx.EXPAND, 0)
        sizer_13.Add(self.button_sim_apply, 0, 0, 0)
        sizer_13.Add((10, 20), 0, 0, 0)
        sizer_13.Add(self.button_sim_ok, 0, 0, 0)
        sizer_13.Add((10, 20), 0, 0, 0)
        sizer_13.Add(self.button_sim_cancel, 0, 0, 0)
        sizer_13.Add((10, 10), 0, 0, 0)
        sizer_12.Add(sizer_13, 0, wx.ALIGN_RIGHT, 0)
        sizer_12.Add((20, 10), 0, 0, 0)
        sizer_6.Add(sizer_12, 2, wx.EXPAND, 0)
        sizer_6.Add((20, 20), 0, 0, 0)
        self.SetSizer(sizer_6)
        self.Layout()
        self.Centre()
        # end wxGlade

    def onSimLoad(self, event): # wxGlade: simSetupDialog.<event_handler>
        print "Event handler `onSimLoad' not implemented!"
        event.Skip()

    def onConfigNew(self, event): # wxGlade: simSetupDialog.<event_handler>
        print "Event handler `onConfigNew' not implemented!"
        event.Skip()

    def onConfigImport(self, event): # wxGlade: simSetupDialog.<event_handler>
        print "Event handler `onConfigImport' not implemented!"
        event.Skip()

    def onConfigDelete(self, event): # wxGlade: simSetupDialog.<event_handler>
        print "Event handler `onConfigDelete' not implemented!"
        event.Skip()

    def onSimNameEdit(self, event): # wxGlade: simSetupDialog.<event_handler>
        print "Event handler `onSimNameEdit' not implemented!"
        event.Skip()

    def onClickAddRobot(self, event): # wxGlade: simSetupDialog.<event_handler>
        print "Event handler `onClickAddRobot' not implemented!"
        event.Skip()

    def onClickConfigureRobot(self, event): # wxGlade: simSetupDialog.<event_handler>
        print "Event handler `onClickConfigureRobot' not implemented!"
        event.Skip()

    def onClickRemoveRobot(self, event): # wxGlade: simSetupDialog.<event_handler>
        print "Event handler `onClickRemoveRobot' not implemented!"
        event.Skip()

    def onClickEditMapping(self, event): # wxGlade: simSetupDialog.<event_handler>
        print "Event handler `onClickEditMapping' not implemented!"
        event.Skip()

    def onClickApply(self, event): # wxGlade: simSetupDialog.<event_handler>
        print "Event handler `onClickApply' not implemented!"
        event.Skip()

    def onClickOK(self, event): # wxGlade: simSetupDialog.<event_handler>
        print "Event handler `onClickOK' not implemented!"
        event.Skip()

# end of class simSetupDialog


class addRobotDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: addRobotDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.label_3 = wx.StaticText(self, -1, "Robot type:")
        self.combo_box_robottype = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN)
        self.label_4 = wx.StaticText(self, -1, "Robot name:")
        self.text_ctrl_robotname = wx.TextCtrl(self, -1, "")
        self.label_5 = wx.StaticText(self, -1, "HANDLERTYPE:")
        self.combo_box_2 = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN)
        self.button_5 = wx.Button(self, -1, "Configure...")
        self.button_7 = wx.Button(self, wx.ID_CANCEL, "")
        self.button_6 = wx.Button(self, wx.ID_OK, "")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.onClickConfigure1, self.button_5)
        self.Bind(wx.EVT_BUTTON, self.onClickOK, self.button_6)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: addRobotDialog.__set_properties
        self.SetTitle("Add/Configure Robot")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: addRobotDialog.__do_layout
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_11 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_9 = wx.BoxSizer(wx.VERTICAL)
        sizer_10 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7.Add(self.label_3, 0, wx.ALL, 5)
        sizer_7.Add(self.combo_box_robottype, 1, wx.ALL, 5)
        sizer_5.Add(sizer_7, 1, wx.EXPAND, 0)
        sizer_8.Add(self.label_4, 0, wx.ALL, 5)
        sizer_8.Add(self.text_ctrl_robotname, 1, wx.ALL, 5)
        sizer_5.Add(sizer_8, 1, wx.EXPAND, 0)
        sizer_10.Add(self.label_5, 0, wx.ALL, 5)
        sizer_10.Add(self.combo_box_2, 1, wx.ALL, 5)
        sizer_10.Add(self.button_5, 0, wx.ALL, 5)
        sizer_9.Add(sizer_10, 1, wx.EXPAND, 0)
        sizer_5.Add(sizer_9, 1, wx.EXPAND, 0)
        sizer_11.Add((20, 20), 1, wx.EXPAND, 0)
        sizer_11.Add(self.button_7, 0, wx.ALL, 5)
        sizer_11.Add(self.button_6, 0, wx.ALL, 5)
        sizer_5.Add(sizer_11, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_5)
        sizer_5.Fit(self)
        self.Layout()
        # end wxGlade

    def onClickConfigure1(self, event): # wxGlade: addRobotDialog.<event_handler>
        print "Event handler `onClickConfigure1' not implemented!"
        event.Skip()

    def onClickOK(self, event): # wxGlade: addRobotDialog.<event_handler>
        print "Event handler `onClickOK' not implemented!"
        event.Skip()

# end of class addRobotDialog


class propMappingDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: propMappingDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER|wx.THICK_FRAME
        wx.Dialog.__init__(self, *args, **kwds)
        self.label_6 = wx.StaticText(self, -1, "Propositions:")
        self.list_box_props = wx.ListBox(self, -1, choices=[], style=wx.LB_SINGLE|wx.LB_ALWAYS_SB)
        self.label_11 = wx.StaticText(self, -1, "Continuous controller mapping:")
        self.text_ctrl_mapping = wx.TextCtrl(self, -1, "")
        self.button_8 = wx.Button(self, -1, u"Edit\n  ↓")
        self.button_9 = wx.Button(self, -1, u"        ↑\nInsert/Apply")
        self.label_7 = wx.StaticText(self, -1, "Robots:")
        self.list_box_robots = wx.ListBox(self, -1, choices=[])
        self.label_8 = wx.StaticText(self, -1, "Sensors/Actuators:")
        self.list_box_functions = wx.ListBox(self, -1, choices=[])
        self.label_10 = wx.StaticText(self, -1, "Parameters:")
        self.button_11 = wx.Button(self, wx.ID_CANCEL, "")
        self.button_10 = wx.Button(self, wx.ID_OK, "")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_LISTBOX, self.onSelectProp, self.list_box_props)
        self.Bind(wx.EVT_BUTTON, self.onClickEdit, self.button_8)
        self.Bind(wx.EVT_BUTTON, self.onClickApply, self.button_9)
        self.Bind(wx.EVT_LISTBOX, self.onSelectRobot, self.list_box_robots)
        self.Bind(wx.EVT_LISTBOX, self.onSelectHandler, self.list_box_functions)
        self.Bind(wx.EVT_BUTTON, self.onClickOK, self.button_10)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: propMappingDialog.__set_properties
        self.SetTitle("Proposition Mapping")
        self.SetSize((836, 616))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: propMappingDialog.__do_layout
        sizer_14 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_16 = wx.BoxSizer(wx.VERTICAL)
        sizer_25 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_19 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_24 = wx.BoxSizer(wx.VERTICAL)
        sizer_21 = wx.BoxSizer(wx.VERTICAL)
        sizer_20 = wx.BoxSizer(wx.VERTICAL)
        sizer_18 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_15 = wx.BoxSizer(wx.VERTICAL)
        sizer_15.Add(self.label_6, 0, wx.LEFT|wx.RIGHT|wx.TOP, 5)
        sizer_15.Add(self.list_box_props, 1, wx.ALL|wx.EXPAND, 5)
        sizer_14.Add(sizer_15, 1, wx.EXPAND, 0)
        sizer_16.Add(self.label_11, 0, wx.ALL, 5)
        sizer_16.Add(self.text_ctrl_mapping, 0, wx.ALL|wx.EXPAND, 5)
        sizer_18.Add((20, 20), 1, wx.EXPAND, 0)
        sizer_18.Add(self.button_8, 0, wx.ALL, 5)
        sizer_18.Add((40, 20), 0, 0, 0)
        sizer_18.Add(self.button_9, 0, wx.ALL, 5)
        sizer_18.Add((20, 20), 1, wx.EXPAND, 0)
        sizer_16.Add(sizer_18, 0, wx.EXPAND, 0)
        sizer_20.Add(self.label_7, 0, wx.ALL, 5)
        sizer_20.Add(self.list_box_robots, 1, wx.ALL|wx.EXPAND, 5)
        sizer_19.Add(sizer_20, 1, wx.EXPAND, 0)
        sizer_21.Add(self.label_8, 0, wx.ALL, 5)
        sizer_21.Add(self.list_box_functions, 1, wx.ALL|wx.EXPAND, 5)
        sizer_19.Add(sizer_21, 1, wx.EXPAND, 0)
        sizer_24.Add(self.label_10, 0, wx.ALL, 5)
        sizer_19.Add(sizer_24, 1, wx.EXPAND, 0)
        sizer_16.Add(sizer_19, 1, wx.EXPAND, 0)
        sizer_25.Add((20, 20), 1, wx.EXPAND, 0)
        sizer_25.Add(self.button_11, 0, wx.ALL, 5)
        sizer_25.Add(self.button_10, 0, wx.ALL, 5)
        sizer_16.Add(sizer_25, 0, wx.EXPAND, 0)
        sizer_14.Add(sizer_16, 2, wx.EXPAND, 0)
        self.SetSizer(sizer_14)
        self.Layout()
        # end wxGlade

    def onSelectProp(self, event): # wxGlade: propMappingDialog.<event_handler>
        print "Event handler `onSelectProp' not implemented!"
        event.Skip()

    def onClickEdit(self, event): # wxGlade: propMappingDialog.<event_handler>
        print "Event handler `onClickEdit' not implemented!"
        event.Skip()

    def onClickApply(self, event): # wxGlade: propMappingDialog.<event_handler>
        print "Event handler `onClickApply' not implemented!"
        event.Skip()

    def onSelectRobot(self, event): # wxGlade: propMappingDialog.<event_handler>
        print "Event handler `onSelectRobot' not implemented!"
        event.Skip()

    def onSelectHandler(self, event): # wxGlade: propMappingDialog.<event_handler>
        print "Event handler `onSelectHandler' not implemented!"
        event.Skip()

    def onClickOK(self, event): # wxGlade: propMappingDialog.<event_handler>
        print "Event handler `onClickOK' not implemented!"
        event.Skip()

# end of class propMappingDialog


if __name__ == "__main__":
    SimConfigEditor = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    SimSetupDialog = simSetupDialog(None, -1, "")
    SimConfigEditor.SetTopWindow(SimSetupDialog)
    SimSetupDialog.Show()
    SimConfigEditor.MainLoop()
