#Imports
import tkinter
import customtkinter
from pytube import YouTube

#Define download function
def start_download():
    try:
        yt_link = link.get()
        print(yt_link)
        yt_object = YouTube(yt_link, on_progress_callback=on_progress)
        video = yt_object.streams.get_highest_resolution()
        video.download()
        title.configure(text = yt_object.title)
        # print("Donwload Complete!")
        finished_label.configure(text="Donwloaded!", text_color = 'green')
    except:
        # print("Error : Link Invalid")
        finished_label.configure(text="Error : Link Invalid!", text_color = "red")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_completed = bytes_downloaded / total_size * 100
    percentage  = str(int(percentage_completed))
    p_percentage.configure(text = percentage + "%")
    progress_bar.set(float(percentage_completed)/100)
    
    p_percentage.update()
    # progress_bar.update()
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

#Finished downloading

finished_label = customtkinter.CTkLabel(app, text="")
finished_label.pack(padx = 5, pady = 5)

#Progressbar & percentage 

p_percentage = customtkinter.CTkLabel(app, text= "0%")
p_percentage.pack()

progress_bar = customtkinter.CTkProgressBar(app,width= 350)
progress_bar.set(0)
progress_bar.pack(padx=10, pady= 10)
#Download Button

download_button = customtkinter.CTkButton(app, width=140, height=28, text="Download", command=start_download)
download_button.pack(padx = 10, pady = 10)

#Run App

app.mainloop()