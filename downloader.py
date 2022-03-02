from tkinter.constants import LEFT
from pytube import YouTube
from pytube import Playlist
import tkinter as tk
from tkinter import Button, Label, PhotoImage, Radiobutton,  Toplevel, mainloop, ttk
from tkinter import filedialog
import os
# --------------------------Class-----------------------------------
class Resolution:
    def highest(self,video,path):
        video.streams.get_highest_resolution().download(path)

    def lowest(self,video,path):
        video.streams.get_lowest_resolution().download(path)

    def mp3(self,video,path):
        video.streams.filter(only_audio=True).first().download(path)

    def custom(self,video,path,res):
        print(res)
        reso = video.streams.get_by_resolution(res)
        reso.download(path)

    def downloaded(self,root):
        sub = Toplevel(root)
        sub.geometry("400x100+290+200")
        sub.title = "downloaded"
        Label(sub, text="Downloaded Successfully", font=("Times", 25),foreground="Green").pack(pady=10)
        Button(sub,text ="Ok",command=sub.destroy,background="red",foreground="white",font=("Helvetica",12)).pack()

# -------------------------------End of the class---------------------------------------------------------
# ---------------------- custom Resolution----------------------
def additional(root):
    sub = Toplevel(root)
    sub.geometry("300x200+620+400")
    sub.title = "Set resolution"
    head = ttk.Label(sub, text="Enter resolution",font=("Times",20)).pack(padx=10)
    global var
    var = tk.StringVar()
    box =  ttk.Entry(sub,font=("courier",15),textvariable=var).pack(pady=20)

    def addb():
            global var
            global FinRes
            FinRes = var.get()
    Button(sub, text="ok", font=('Georgia',15),command=lambda: [addb(), sub.destroy()]).pack()

# -----------------------------------------------------------------------------------
root = tk.Tk()
bg = PhotoImage(file="youtube-logo-png-2075.png")
root.title("YTV downloader")
root.minsize(800,600)
path = ''
var = tk.StringVar()
FinRes = ''
BackGround = Label(root,image=bg).place(x=0,y=0)
Label(root,text="YTV DOWNLOADER",font=("Times",36),foreground="red").pack(padx=10)
#--------------------Browse files-----------------------
def fold():
    global path
    path = filedialog.askdirectory()
    if(path == ''):
        temp['text'] = os.getcwd()
    else:
        temp['text'] = path
Label(root,text="Storage location:",font='Arial').pack(padx=10)
temp = Label(root,text= os.getcwd(),background="white")
temp.pack()
Button(root, text="Change", command=fold, font=("Georgia", 10)).pack(pady=10)
#----------------------End of browse files---------------------------------

#---------------------URL Error--------------------------------
def urlerror(res=False):
    sub = Toplevel(root)
    if(res):
        sub.geometry("400x100+200+100")
        sub.title = "Resolution Error"
        label = Label(sub, text="Resolution cannot be empty", font=(
            "Times", 25), foreground="Red")
        label.pack(pady=10)
        Button(sub, text="Ok", command= lambda:[sub.destroy(),cmd()], background="red",
        foreground="white", font=("Helvetica", 12)).pack()
    else:
        sub.geometry("400x100+90+10")
        sub.title = "URL Error"
        label = Label(sub, text="Enter a valid URL", font=(
        "Times", 25), foreground="Red")
        label.pack(pady=10)
        Button(sub, text="Ok", command=sub.destroy, background="red",
        foreground="white", font=("Helvetica", 12)).pack()
# ------------------------------------------------------------
url = ""
res = 1
num = 1
def playlist():
    skip = True
    try:
        pl = Playlist(url)
    except:
        skip = False
        urlerror()
    obj = Resolution()
    count = 0
    num = 1
    if skip:
        for v in pl.videos:
            if(res == 1):
                obj.highest(v,path)
            elif(res == 2):
                obj.lowest(v,path)
            elif(res == 3):
                obj.mp3(v,path)
            else:
                try:
                    if(FinRes == ''):
                        count += 1
                        urlerror(True)
                    else:
                        obj.custom(v,path,FinRes)
    
                except:
                    count += 1
                    sub = Toplevel(root)
                    sub.geometry("400x100+90+10")
                    sub.title = "downloaded"
                    Label(sub, text="Resolution Unavailable", font=("Times", 25), foreground="Red").pack(pady=10)
                    Button(sub, text="Ok", command=sub.destroy, background="red",foreground="white", font=("Helvetica", 12)).pack()
            num += 1

        if(count == 0):
            obj.downloaded(root)
        count = 0

def single():
    skip = True
    obj = Resolution()
    try:
        v = YouTube(url) 
    except:
        skip = False
        urlerror()
    if skip:
        count = 0
        if(res == 1):
            obj.highest(v, path)
        elif(res == 2):
            obj.lowest(v,path)
        elif(res == 3):
            obj.mp3(v,path)
        else:
            try:
                if(FinRes == ''):
                        count += 1
                        urlerror(True)
                else:
                    obj.custom(v,path,FinRes)
            except:
                count = 1
                sub = Toplevel(root)
                sub.geometry("400x100+290+200")
                sub.title = "downloaded"
                Label(sub, text="Resolution Unavailable", font=(
                    "Times", 25), foreground="Red").pack(pady=10)
                Button(sub, text="Ok", command=sub.destroy, background="red",
                    foreground="white", font=("Helvetica", 12)).pack()
        if(count == 0):
            obj.downloaded(root)
        count = 0

#----------------palylist vs single button---------------------
def pVs():
    global num
    num = va.get()

va = tk.IntVar()
va.set(1)
bt1 = Radiobutton(root, text='Single video   ',variable=va,value=1,command=pVs,font=("Times New Roman",18))
bt2 = Radiobutton(root,text='Whole playlist',variable=va,value=2,command=pVs,font=("Times New Roman",18))
bt1.pack(padx=10,pady=10)
bt2.pack(padx=10,pady=10)
#------------------------------------------------------------------
# ------------------text box------------------------------
label = ttk.Label(root, font = ("Times", 25), text="Enter URL")
label.pack(padx=10,pady=10)
name = tk.StringVar()
nameEntered = ttk.Entry(root,width=25,font = ('courier',20) ,textvariable=name)
nameEntered.pack()
def calls():
    if(int(num) == 1):
        single()
    else:
        playlist()
def urlbox():
    global url
    url = name.get()
    print(type(name))
    calls()
#---------------------------------------------------------------
#-------------Resolution button-------------------------------
def cmd():
    global res
    res = r.get()
    if res == 4:
        additional(root)
        
r = tk.IntVar()
r.set(1)
values = {"Highest resolution           ":'1',
            "Lowest resolution          ":'2',
            "Audio only format          ":'3',
            "Custom resolution":'4'
}
for(text,value) in values.items():
    Radiobutton(root,value=value,text=text,variable=r,command=cmd,font=("Bahnschrift SemiBold",15),background="white").pack(side = LEFT,ipady=0,ipadx=40)
#------------------------------------------------------------

#--------------download Button----------------------------
def call():
    if(int(num) == 1):
        single()
    else:
        playlist()
tem = Button(root, text="Download", command = urlbox, height=0, width=8, background="red", foreground="white", font=("ALTERNATE GOTHIC", 15))
tem.place(x=600,y=400)
mainloop()