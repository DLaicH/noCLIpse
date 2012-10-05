#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.4 on Mon Sep 17 02:02:44 2012


#Makes use of wxPython (http://wxpython.org/) py-AndroidBuild (https://github.com/miracle2k/py-androidbuild)
#Interface built with wxGlade 0.6.4 (http://wxglade.sourceforge.net/)

from android.build import AndroidProject, get_platform, ProgramFailedError
import atexit
import cPickle
import logging
import os.path
import platform
from subprocess import Popen, check_output
import wx

# begin wxGlade: extracode
# end wxGlade

#Configuration variables for py-androidbuild
logging.getLogger('py-androidbuild').addHandler(logging.StreamHandler())

#Starting multi-platform specific code.
print platform.system()
if platform.system() == "Windows":
    androidpath = "/tools/android.bat"
    extension = ".bat"
else:
    androidpath = "/tools/android"
    extension = ""

class StringDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: StringDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER | wx.THICK_FRAME | wx.STAY_ON_TOP
        wx.Dialog.__init__(self, *args, **kwds)
        self.panel_1 = wx.ScrolledWindow(self, -1, style=wx.TAB_TRAVERSAL)
        self.targets = wx.StaticText(self.panel_1, -1, "")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade
        

    def __set_properties(self):
        # begin wxGlade: StringDialog.__set_properties
        self.SetSize((400, 300))
        self.panel_1.SetScrollRate(10, 10)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: StringDialog.__do_layout
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6.Add(self.targets, 0, 0, 0)
        self.panel_1.SetSizer(sizer_6)
        sizer_4.Add(self.panel_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_4)
        self.Layout()
        # end wxGlade

    def loadTargets(self):
        targets_string = check_output([config.sdk_path+androidpath, "list", "targets"])
        print get_platform(config.sdk_path, None)
        #print targets_string
        self.targets.SetLabel(targets_string)

    def setBody(self, text):
        self.targets.SetLabel(text)

# end of class StringDialog

class LibDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: LibDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.list_box_2 = wx.ListBox(self, -1, choices=[], style=wx.LB_MULTIPLE)
        self.label_6 = wx.StaticText(self, -1, "Other")
        self.text_ctrl_5 = wx.TextCtrl(self, -1, "")
        self.button_2 = wx.Button(self, wx.ID_OK, "")
        self.button_3 = wx.Button(self, wx.ID_CANCEL, "")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: LibDialog.__set_properties
        self.SetTitle("Add Library")
        self.SetSize((300, 250))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: LibDialog.__do_layout
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5.Add(self.list_box_2, 1, wx.EXPAND, 0)
        sizer_8.Add(self.label_6, 0, wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_8.Add(self.text_ctrl_5, 1, 0, 0)
        sizer_5.Add(sizer_8, 0, wx.EXPAND, 0)
        sizer_7.Add(self.button_2, 0, 0, 0)
        sizer_7.Add((10, 5), 0, 0, 0)
        sizer_7.Add(self.button_3, 0, 0, 0)
        sizer_5.Add(sizer_7, 0, wx.TOP | wx.ALIGN_CENTER_HORIZONTAL, 10)
        self.SetSizer(sizer_5)
        self.Layout()
        # end wxGlade

# end of class LibDialog

class noCLIpseFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: noCLIpseFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        
        # Menu Bar
        self.main_frame_menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(wx.NewId(), "New Project", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(wx.NewId(), "New Lib Project", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(wx.NewId(), "Open Existing", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendSeparator()
        self.menu_project_save = wx.MenuItem(wxglade_tmp_menu, wx.NewId(), "Save Project\tCTRL+S", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.menu_project_save)
        wxglade_tmp_menu.AppendSeparator()
        wxglade_tmp_menu.Append(wx.NewId(), "Build and Install", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(wx.NewId(), "Add Library Project", "", wx.ITEM_NORMAL)
        self.main_frame_menubar.Append(wxglade_tmp_menu, "Project")
        wxglade_tmp_menu = wx.Menu()
        self.settings_change_sdk = wx.MenuItem(wxglade_tmp_menu, wx.NewId(), "Change Android SDK Path", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.settings_change_sdk)
        self.settings_change_workspace = wx.MenuItem(wxglade_tmp_menu, wx.NewId(), "Change Workspace Path", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.settings_change_workspace)
        self.main_frame_menubar.Append(wxglade_tmp_menu, "Settings")
        wxglade_tmp_menu = wx.Menu()
        self.android_launch_sdk = wx.MenuItem(wxglade_tmp_menu, wx.NewId(), "Android SDK Manager", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.android_launch_sdk)
        self.android_launch_avd = wx.MenuItem(wxglade_tmp_menu, wx.NewId(), "AVD Manager", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.android_launch_avd)
        self.android_launch_ddms = wx.MenuItem(wxglade_tmp_menu, wx.NewId(), "Dalvik Debug Monitor (DDMS)", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.android_launch_ddms)
        self.main_frame_menubar.Append(wxglade_tmp_menu, "Android")
        self.SetMenuBar(self.main_frame_menubar)
        # Menu Bar end
        self.tab_notebook = wx.Notebook(self, -1, style=0)
        self.project_tab = wx.Panel(self.tab_notebook, -1)
        self.project_window = wx.SplitterWindow(self.project_tab, -1, style=wx.SP_3D | wx.SP_BORDER)
        self.project_list_pane = wx.Panel(self.project_window, -1)
        self.project_list = wx.ListBox(self.project_list_pane, -1, choices=["<New Project>"], style=wx.LB_SORT)
        self.project_details_pane = wx.Panel(self.project_window, -1)
        self.project_name_label = wx.StaticText(self.project_details_pane, -1, "Project Name (optional)")
        self.project_name = wx.TextCtrl(self.project_details_pane, -1, "")
        self.project_target_label = wx.StaticText(self.project_details_pane, -1, "Target Number")
        self.list_targets = wx.Choice(self.project_details_pane, -1, choices=[])
        self.list_targets_button = wx.Button(self.project_details_pane, -1, "List Targets")
        self.project_path_label = wx.StaticText(self.project_details_pane, -1, "Project Path")
        self.project_path = wx.DirPickerCtrl(self.project_details_pane, -1, homedir, "Select a path for this project", style=wx.DIRP_USE_TEXTCTRL)
        self.activity_name_label = wx.StaticText(self.project_details_pane, -1, "Activity Name")
        self.activity_name = wx.TextCtrl(self.project_details_pane, -1, "")
        self.project_package_label = wx.StaticText(self.project_details_pane, -1, "Package")
        self.project_package = wx.TextCtrl(self.project_details_pane, -1, "")
        self.save_project = wx.Button(self.project_details_pane, -1, "Save Project")
        self.building_split_window = wx.SplitterWindow(self.project_details_pane, -1, style=wx.SP_3D | wx.SP_BORDER)
        self.build_path_pane = wx.Panel(self.building_split_window, -1)
        self.build_path_staticbox = wx.StaticBox(self.build_path_pane, -1, "Build Path")
        self.building_pane = wx.Panel(self.building_split_window, -1)
        self.build_type_label = wx.StaticText(self.building_pane, -1, "Build Type")
        self.build_type_choice = wx.Choice(self.building_pane, -1, choices=["Debug", "Release"])
        self.keystore_label = wx.StaticText(self.building_pane, -1, "Keystore")
        self.keystore_filedialog = wx.FilePickerCtrl(self.building_pane, -1)
        self.alias_label = wx.StaticText(self.building_pane, -1, "Alias")
        self.alias = wx.TextCtrl(self.building_pane, -1, "")
        self.password_label = wx.StaticText(self.building_pane, -1, "Password")
        self.password = wx.TextCtrl(self.building_pane, -1, "", style=wx.TE_PASSWORD)
        self.build_button = wx.Button(self.building_pane, -1, "Build Project")
        self.libproject_tab = wx.Panel(self.tab_notebook, -1)
        self.libproject_window = wx.SplitterWindow(self.libproject_tab, -1, style=wx.SP_3D | wx.SP_BORDER)
        self.libproject_list_pane = wx.Panel(self.libproject_window, -1)
        self.libproject_list = wx.ListBox(self.libproject_list_pane, -1, choices=["<New Lib Project>"], style=wx.LB_SORT)
        self.libproject_details_pane = wx.Panel(self.libproject_window, -1)
        self.libproject_name_label = wx.StaticText(self.libproject_details_pane, -1, "Lib Project Name (optional)")
        self.libproject_name = wx.TextCtrl(self.libproject_details_pane, -1, "")
        self.libproject_target_label = wx.StaticText(self.libproject_details_pane, -1, "Target Number")
        self.libproject_target = wx.TextCtrl(self.libproject_details_pane, -1, "")
        self.lib_list_targets_button = wx.Button(self.libproject_details_pane, -1, "List Targets")
        self.libproject_path_label = wx.StaticText(self.libproject_details_pane, -1, "Lib Project Path")
        self.libproject_path = wx.DirPickerCtrl(self.libproject_details_pane, -1, homedir, "Select a path for this library project", style=wx.DIRP_USE_TEXTCTRL)
        self.libproject_package_label = wx.StaticText(self.libproject_details_pane, -1, "Package")
        self.libproject_package = wx.TextCtrl(self.libproject_details_pane, -1, "")
        self.save_libproject = wx.Button(self.libproject_details_pane, -1, "Save Library Project")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_MENU, self.save_project_handler, self.menu_project_save)
        self.Bind(wx.EVT_MENU, self.change_sdk_path, self.settings_change_sdk)
        self.Bind(wx.EVT_MENU, self.change_workspace_path, self.settings_change_workspace)
        self.Bind(wx.EVT_MENU, self.launch_android, self.android_launch_sdk)
        self.Bind(wx.EVT_MENU, self.launch_avd, self.android_launch_avd)
        self.Bind(wx.EVT_MENU, self.launch_ddms, self.android_launch_ddms)
        self.Bind(wx.EVT_BUTTON, self.list_targets_handler, self.list_targets_button)
        self.Bind(wx.EVT_BUTTON, self.save_project_handler, self.save_project)
        self.Bind(wx.EVT_CHOICE, self.build_type_switch, self.build_type_choice)
        self.Bind(wx.EVT_BUTTON, self.build_project, self.build_button)
        self.Bind(wx.EVT_BUTTON, self.list_targets_handler, self.lib_list_targets_button)
        self.Bind(wx.EVT_BUTTON, self.save_project_handler, self.save_libproject)
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.changed_tab_handler, self.tab_notebook)
        # end wxGlade

        #self.project_path.Destroy()
        #self.project_path = wx.DirPickerCtrl(self.project_details_pane, -1, homedir, "Select a path for this project", style=wx.DIRP_DEFAULT_STYLE)
        self.targets_panel = StringDialog(self, -1, "Target List")
        self.results_panel = StringDialog(self, -1, "Results")
        self.sdk_path_dialog = wx.DirDialog(self, "Please choose a valid Android SDK path", homedir, wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)

        self.switch_build_type()

    def __set_properties(self):
        # begin wxGlade: noCLIpseFrame.__set_properties
        self.SetTitle("noCLIpse Android Project Manager")
        self.SetSize((800, 600))
        self.project_list.SetSelection(0)
        self.build_type_choice.SetSelection(0)
        self.libproject_list.SetSelection(0)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: noCLIpseFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        libproject_sizer = wx.BoxSizer(wx.VERTICAL)
        libproject_details_sizer = wx.BoxSizer(wx.VERTICAL)
        libproject_details = wx.FlexGridSizer(4, 2, 0, 0)
        sizer_3_copy = wx.BoxSizer(wx.HORIZONTAL)
        libproject_list_sizer = wx.BoxSizer(wx.VERTICAL)
        project_sizer = wx.BoxSizer(wx.VERTICAL)
        project_details_sizer = wx.BoxSizer(wx.VERTICAL)
        build_details = wx.FlexGridSizer(5, 2, 1, 1)
        self.build_path_staticbox.Lower()
        build_path = wx.StaticBoxSizer(self.build_path_staticbox, wx.HORIZONTAL)
        grid_sizer_1 = wx.FlexGridSizer(3, 2, 0, 0)
        project_details = wx.FlexGridSizer(5, 2, 0, 0)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        project_list_sizer = wx.BoxSizer(wx.VERTICAL)
        project_list_sizer.Add(self.project_list, 1, wx.EXPAND, 0)
        self.project_list_pane.SetSizer(project_list_sizer)
        project_details.Add(self.project_name_label, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        project_details.Add(self.project_name, 0, wx.EXPAND, 0)
        project_details.Add(self.project_target_label, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_3.Add(self.list_targets, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_3.Add(self.list_targets_button, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        project_details.Add(sizer_3, 1, wx.EXPAND, 0)
        project_details.Add(self.project_path_label, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        project_details.Add(self.project_path, 1, wx.EXPAND, 0)
        project_details.Add(self.activity_name_label, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        project_details.Add(self.activity_name, 0, wx.EXPAND, 0)
        project_details.Add(self.project_package_label, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        project_details.Add(self.project_package, 0, wx.EXPAND, 0)
        project_details.AddGrowableCol(1)
        project_details_sizer.Add(project_details, 0, wx.EXPAND, 0)
        project_details_sizer.Add(self.save_project, 0, wx.TOP, 20)
        build_path.Add(grid_sizer_1, 1, wx.EXPAND, 0)
        self.build_path_pane.SetSizer(build_path)
        build_details.Add(self.build_type_label, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        build_details.Add(self.build_type_choice, 0, 0, 0)
        build_details.Add(self.keystore_label, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        build_details.Add(self.keystore_filedialog, 1, wx.EXPAND, 0)
        build_details.Add(self.alias_label, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        build_details.Add(self.alias, 0, wx.EXPAND, 0)
        build_details.Add(self.password_label, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        build_details.Add(self.password, 0, wx.EXPAND, 0)
        build_details.Add(self.build_button, 0, wx.ALIGN_RIGHT, 0)
        self.building_pane.SetSizer(build_details)
        build_details.AddGrowableCol(1)
        self.building_split_window.SplitVertically(self.build_path_pane, self.building_pane, 16)
        project_details_sizer.Add(self.building_split_window, 1, wx.EXPAND, 0)
        self.project_details_pane.SetSizer(project_details_sizer)
        self.project_window.SplitVertically(self.project_list_pane, self.project_details_pane, 106)
        project_sizer.Add(self.project_window, 1, wx.EXPAND, 0)
        self.project_tab.SetSizer(project_sizer)
        libproject_list_sizer.Add(self.libproject_list, 1, wx.EXPAND, 0)
        self.libproject_list_pane.SetSizer(libproject_list_sizer)
        libproject_details.Add(self.libproject_name_label, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        libproject_details.Add(self.libproject_name, 0, wx.EXPAND, 0)
        libproject_details.Add(self.libproject_target_label, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_3_copy.Add(self.libproject_target, 0, 0, 0)
        sizer_3_copy.Add(self.lib_list_targets_button, 0, 0, 0)
        libproject_details.Add(sizer_3_copy, 1, wx.EXPAND, 0)
        libproject_details.Add(self.libproject_path_label, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        libproject_details.Add(self.libproject_path, 1, wx.EXPAND, 0)
        libproject_details.Add(self.libproject_package_label, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        libproject_details.Add(self.libproject_package, 0, wx.EXPAND, 0)
        libproject_details.AddGrowableCol(1)
        libproject_details_sizer.Add(libproject_details, 0, wx.EXPAND, 0)
        libproject_details_sizer.Add(self.save_libproject, 0, wx.TOP, 20)
        self.libproject_details_pane.SetSizer(libproject_details_sizer)
        self.libproject_window.SplitVertically(self.libproject_list_pane, self.libproject_details_pane, 122)
        libproject_sizer.Add(self.libproject_window, 1, wx.EXPAND, 0)
        self.libproject_tab.SetSizer(libproject_sizer)
        self.tab_notebook.AddPage(self.project_tab, "Projects")
        self.tab_notebook.AddPage(self.libproject_tab, "Library Projects")
        sizer_1.Add(self.tab_notebook, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade
        self.project_window.SetMinimumPaneSize(150)
        self.libproject_window.SetMinimumPaneSize(150)
        self.building_split_window.SetMinimumPaneSize(250)

    def Show(self):
        while not os.path.isfile(config.sdk_path+androidpath):
            print config.sdk_path + androidpath + " does not contain the SDK"
            new_path = wx.DirSelector("Select the directory where the Android SDK is installed", homedir)
            if not new_path:
                self.Close()
                break
            config.sdk_path = new_path
            print "changing to " + config.sdk_path

        self.targets_panel.loadTargets()
        wx.Frame.Show(self)

    def save_project_handler(self, event):  # wxGlade: noCLIpseFrame.<event_handler>
        #event_type = event.GetEventType()
        #if event_type == wx.EVT_COMMAND_BUTTON_CLICKED:
        #    print "save button";
        #elif event_type == wx.EVT_COMMAND_MENU_SELECTED:
        #    print "save menu";

        current_tab = self.tab_notebook.GetCurrentPage()
        if current_tab == self.project_tab:
            command = [config.sdk_path+androidpath, "create", "project"]
            command.extend(["--target", self.project_target.GetValue()])
            command.extend(["--path", self.project_path.GetPath()])
            command.extend(["--activity", self.activity_name.GetValue()])
            command.extend(["--package", self.project_package.GetValue()])

            name = self.project_name.GetValue()
            if name: command.extend(["--name", name])
        elif current_tab == self.libproject_tab:
            print "lib project"
            command = [config.sdk_path+androidpath, "create", "lib-project"]
            command.extend(["--target", self.libproject_target.GetValue()])
            command.extend(["--path", self.libproject_path.GetPath()])
            command.extend(["--package", self.libproject_package.GetValue()])
            
            name = self.libproject_name.GetValue()
            if name: command.extend(["--name", name])

        if len(command) >= 9:
            #Popen([config.sdk_path+androidpath, "create", "project","--target","3", "--path","C:\Users\Dawson Goodell\New Folder", "--activity","testact", "--package","com.osmstudios.test"])

            print command
            results = Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read()
            print results
            self.results_panel.setBody(results)
            self.results_panel.Show()

    def changed_tab_handler(self, event):  # wxGlade: noCLIpseFrame.<event_handler>
        print "Event handler `changed_tab_handler' not implemented"
        print "But it works, so who really cares?"

    def list_targets_handler(self, event):  # wxGlade: noCLIpseFrame.<event_handler>
        self.targets_panel.Show()

    def change_sdk_path(self, event):  # wxGlade: noCLIpseFrame.<event_handler>
        new_path = ""
        while not os.path.isfile(new_path+androidpath):
            new_path = wx.DirSelector("Select the directory where the Android SDK is installed", config.sdk_path)
            if not new_path:
                return

        config.sdk_path = new_path

        self.targets_panel.loadTargets()

    def change_workspace_path(self, event):  # wxGlade: noCLIpseFrame.<event_handler>
        new_path = ""
        while not os.path.isdir(new_path):
            new_path = wx.DirSelector("Select the workspace directory to scan for existing projects", config.workspace_path)
            if not new_path:
                return

        config.workspace_path = new_path

    def launch_android(self, event):  # wxGlade: noCLIpseFrame.<event_handler>
        Popen(config.sdk_path+androidpath)

    def launch_avd(self, event):  # wxGlade: noCLIpseFrame.<event_handler>
        Popen([config.sdk_path+androidpath, "avd"])

    def launch_ddms(self, event):  # wxGlade: noCLIpseFrame.<event_handler>
        Popen(config.sdk_path+"/tools/ddms"+extension)

    def switch_build_type(self):
        if self.build_type_choice.GetCurrentSelection() == 0:
            self.keystore_filedialog.Disable()
            self.alias.Disable()
            self.password.Disable()
        else:
            self.keystore_filedialog.Enable()
            self.alias.Enable()
            self.password.Enable()

    def build_type_switch(self, event):  # wxGlade: noCLIpseFrame.<event_handler>
        self.switch_build_type()

    def build_project(self, event):  # wxGlade: noCLIpseFrame.<event_handler>
        print "Building - " + self.project_path.GetPath() + "/AndroidManifest.xml with " + config.sdk_path

        if self.build_type_choice.GetCurrentSelection() == 0:
            keystore_val = "debug.keystore"
            keystore_alias = "androiddebugkey"
            keystore_password = "android"
        else:
            print "Release building not yet implemented"
            keystore_val = "debug.keystore"
            keystore_alias = "androiddebugkey"
            keystore_password = "android"
        
        project = AndroidProject(self.project_path.GetPath() + '/AndroidManifest.xml',sdk_dir=config.sdk_path)
        try:
            project.build()
        except ProgramFailedError, e:
            print e.cmdline
            print e.returncode
            print e.stderr
            print e.stdout

# end of class noCLIpseFrame

#set up a dummy class for the config object
class Generic:
    pass

#write the config file on exit
def write_config():
    print "writing config"
    conf_file = open(".config", "wb")
    cPickle.dump(config, conf_file)
    conf_file.close()


#this grabs the user's directory in both windows and linux
homedir = os.path.expanduser("~")
homedir = homedir.replace("\\","/")

#check if the config file exists
if os.path.isfile(".config"):
    read_conf = open(".config", "rb")
    config = cPickle.load(read_conf)
    read_conf.close()
    print "conf exists"
    #print config.workspace_path
    print config.sdk_path
else:
    #init the config object
    config = Generic()

    #this will need changed to Eclipse's default path in Windows
    workspace_path = homedir+"/workspace"
    print workspace_path
    #does the workspace path exist?
    if os.path.isdir(workspace_path):
        config.workspace_path = workspace_path
        print "workspace exists"
    else:
        print "workspace doesn't exist"

    #the default Android SDK directory in linux
    config.sdk_path = homedir+"/android-sdk-linux"
    print "search for SDK at " + config.sdk_path

    config.projects = []
    config.libprojects = []

atexit.register(write_config)

if __name__ == "__main__":
    neCLI = wx.PySimpleApp(0)
    neCLI.Bind(wx.EVT_END_SESSION, write_config)
    wx.InitAllImageHandlers()
    main_frame = noCLIpseFrame(None, -1, "")
    neCLI.SetTopWindow(main_frame)
    main_frame.Show()
    neCLI.MainLoop()
