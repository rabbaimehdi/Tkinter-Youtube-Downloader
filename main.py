#Imports
import tkinter
import customtkinter
from pytube import YouTube

#Define download function
def start_download():
    try:
        yt_link = link.get()
        yt_object = YouTube(yt_link)
        video = yt_object.streams.get_highest_resolution()
        video.download()
        print("Donwload Complete!")
    except:
        print("Error : Link Invalid")
#Settings

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

#App Frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

#App widgets
title = customtkinter.CTkLabel(app,text="Insert a youtube link")
title.pack(padx = 10, pady = 10)

#Link Input
url = tkinter.StringVar()
link = customtkinter.CTkEntry(app,width= 350, height=30, placeholder_text="Paste youtube link here", textvariable=url)
link.pack()

#Download Button

download_button = customtkinter.CTkButton(app, width=140, height=28, text="Download", command=start_download)
download_button.pack(padx = 10, pady = 10)

#Run App

app.mainloop()