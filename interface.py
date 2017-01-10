# Pype Cleaner
# File: interface.py
# Description:
#   Provide GUI for Py Cleaner, using Tkinter
#
# Name: Carlos Rivera
# Date: July 29, 2016

import os
try:
    # for Python2
    import Tkinter as tk
except ImportError:
    # for Python3
    import tkinter as tk
else:
    print('ERROR. Having problems importing Tkinter. Check that you have Tkinter.')

TITLE_FONT = ("Helvetica", 18, "bold")


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        title_label = tk.Label(self, text="Welcome to Pype Cleaner", font=TITLE_FONT)
        title_label.pack(side="top", fill="x", pady=10)

        desc_label = tk.Label(self, text="This app is designed to allow easier"
                                         " deletion of multiple files within the"
                                         " Desktop directory. Optimized for mac", wraplength=300, pady=10)
        desc_label.pack()

        # to delete screen
        button1 = tk.Button(self, text="Begin",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        # to quit app
        quit_button = tk.Button(self, text="Quit", command=quit)
        button1.pack()
        button2.pack()
        quit_button.pack()

        label = tk.Label(self, text="Copyright Carlos Rivera 2016")
        label.pack()


class PageOne(tk.Frame):

    #direct_label = tk.StringVar()

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # title and description
        title = tk.Label(self, text="Deletion Center", font=TITLE_FONT)
        title.pack(side="top", fill="x", pady=10)
        description = tk.Label(self, text="Left List contains: Directories\n"
                                          "Right List contains: Files")
        description.pack()

        # display current location
        # direct_label.set("Currently at {}.".format(os.getcwd()))
        self.current_directory_label = tk.Label(self, text="Currently at {}".format(os.getcwd()))
        self.current_directory_label.pack()

        # directory_label = tk.Label(self, text=self.direct_label, wraplength=300, pady=10)
        # directory_label.pack()

        # display files currently in directory
        directory_listbox = tk.Listbox(self)
        directory_listbox.pack(side=tk.LEFT)

        # display files currently in directory
        files_listbox = tk.Listbox(self)
        files_listbox.pack(side=tk.RIGHT)

        # create directory and file lists
        for root, subdirs, files in os.walk(os.getcwd()):
            for idx, directory in enumerate(subdirs):
                directory_listbox.insert(idx, directory)
            for idx, file in enumerate(files):
                files_listbox.insert(idx, file)

        # go up one level button
        dir_up_button = tk.Button(self, text="Go Up One Level", command=self.change_directory_up())
        dir_up_button.pack()

        # go back to home menu
        home_button = tk.Button(self, text="Back", command=lambda: controller.show_frame("StartPage"))
        home_button.pack()

    def change_directory_up(self):
        # parent = os.path.join(os.getcwd(), "..")  # construct a path to parent
        # os.chdir(parent)

        os.chdir(os.path.dirname(os.getcwd()))

        self.current_directory_label.config(text="Currently at {}".format(os.getcwd()))

        # allow permission to modify directory


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.wm_title("Pype Cleaner")
    app.mainloop()