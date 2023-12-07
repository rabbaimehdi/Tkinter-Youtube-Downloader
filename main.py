#Imports
import tkinter
import customtkinter
from pytube import YouTube

#Settings

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#App Frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

#App widgets
Title = customtkinter.CTkLabel(app,text="Insert a youtube link")
Title.pack()

#Run App

app.mainloop()