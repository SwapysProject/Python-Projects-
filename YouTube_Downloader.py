from tkinter import *
from pytube import YouTube
r=Tk()
r.geometry('500x300')
r.resizable(0,0)
r.title("Swapys YouTube video downloader")
Label(r,text = 'Youtube Video Downloader', font = 'arial 20 bold').pack()
link = StringVar()
Label(r,text="paste link here:",font='arial 15 bold').place(x=160,y=60)
link_enter= Entry(r,width=70,textvariable=link).place(x=32,y=90)
def downloader():
    url=YouTube(str(link.get()))
    video= url.streams.get_highest_resolution()
    video.download()
    Label(r,text="downloaded successfuly",font="arial 15 bold",bg='yellow',padx=2,command=downloader).place(x=180,y=150)
Button(r,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = downloader).place(x=180 ,y = 150)
r.mainloop()

