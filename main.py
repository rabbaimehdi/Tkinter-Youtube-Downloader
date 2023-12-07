#Imports
import tkinter
import customtkinter
from pytube import YouTube

#Define download function
def start_download():
    try:
        yt_link = link.get()
        print(yt_link)
        yt_object = YouTube(yt_link)
        video = yt_object.streams.get_highest_resolution()
        video.download()
        title.configure(text = yt_object.title)
        # print("Donwload Complete!")
        finished_label.configure(text="Donwloaded!", text_color = 'green')
    except:
        # print("Error : Link Invalid")
        finished_label.configure(text="Error : Link Invalid!", text_color = "red")
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

#Video title after download

finished_label = customtkinter.CTkLabel(app, text="")
finished_label.pack(padx = 5, pady = 5)

#Download Button

download_button = customtkinter.CTkButton(app, width=140, height=28, text="Download", command=start_download)
download_button.pack(padx = 10, pady = 10)

#Run App

app.mainloop()