from tkinter import *
import tkinter.messagebox
from subprocess import check_output

class ytdownloadApp:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack(fill=None, expand=False)

        self.txtLbl = Label(frame, text='Youtube-dl for dummies!')
        self.urlTxt = Entry(frame, textvariable='valueTxt')
        self.urlBtn = Button(frame, text="Converter", command=self.downloadVideo)

        self.txtLbl.pack(side=TOP)
        self.urlTxt.pack(side=LEFT, ipady=3, ipadx=100, padx=5)
        self.urlBtn.pack(side=LEFT)

    def clear_text(self):
        self.urlTxt.delete(0, 'end')

    def downloadVideo(self):
        url = self.urlTxt.get()

        if url.strip() == "":
            tkinter.messagebox.showerror('Too Noob', 'Enter a valid url.')
            self.clear_text()
        else:
            fullcommand = str("youtube-dl " + url)

            try:
                check_output(fullcommand , shell=True).decode()
            except:
                tkinter.messagebox.showerror('Too Noob', '\'' + url + '\'' + ' is not a valid URL.')
                self.clear_text()

root = Tk()
icon = PhotoImage(file='icon.png')
root.tk.call('wm', 'iconphoto', root._w, icon)
root.geometry("400x50")
root.resizable(width=False,height=False)
root.grid_propagate(False)
root.wm_title('Simple Converter YT to MP4')
App = ytdownloadApp(root)
root.mainloop()