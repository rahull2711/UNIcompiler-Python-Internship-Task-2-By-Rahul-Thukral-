from os import path
from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from tkinter import messagebox

import shutil #Importing shutil module which helps in moving video to the desired location that user has selected

def reset_urlandlocation(): #function for reseting the path of download and url
    url_entry.delete(0,END)
    dirpath_lab.configure(text="SELECT PATH TO DOWNLOAD")

def browse_button(): # function for browsing various locations to download the video in a particular location
    path = filedialog.askdirectory()
    dirpath_lab.configure(text=path)

def download360p():
    url=url_entry.get()
    yt_path = dirpath_lab.cget("text") #getting the location where the video needs to be downloaded
    
    try: #downloading the video of selected resolution
        root.title('Downloading the youtube video...')
        ys=YouTube(url).streams.filter(resolution="360p") #downloading in 360p
        yt_video= ys.first().download() #downloading
        shutil.move(yt_video,yt_path)  #moving video to the required path selected by user
        root.title('VIDEO Download Completed!!')
        messagebox.showinfo('DOWNLOADED','Youtube Video Downloaded!!')#messagebox for confirmation of download
    except Exception as e: #if download could not be completed due to any exception or error, it will be displayed in a messagebox 
        messagebox.showerror('Error',e)
def download240p():
    url=url_entry.get()
    yt_path = dirpath_lab.cget("text") #getting the location where the video needs to be downloaded
    
    try: #downloading the video of selected resolution
        root.title('Downloading the youtube video...')
        ys=YouTube(url).streams.filter(resolution="240p") #downloading in 240p
        yt_video= ys.first().download()#downloading
        shutil.move(yt_video,yt_path)  #moving video to the required path selected by user
        root.title('VIDEO Download Completed!!')
        messagebox.showinfo('DOWNLOADED','Youtube Video Downloaded!!')#messagebox for confirmation of download
    except Exception as e: #if download could not be completed due to any exception or error, it will be displayed in a messagebox 
        messagebox.showerror('Error',e)

def download_highestres(): #function for downloading video in highest resolution available for a particular youtube video
    url = url_entry.get()
    yt_path = dirpath_lab.cget("text") #getting the location where the video needs to be downloaded
    try:
        root.title('Downloading the youtube video...')
        yt_video = YouTube(url).streams.get_highest_resolution().download() #downloading in highest resolution
        shutil.move(yt_video,yt_path)  #moving video to the required path selected by user
        root.title('VIDEO Download Completed!!')
        messagebox.showinfo('DOWNLOADED','Youtube Video Downloaded!!')#messagebox for confirmation of download
    except Exception as e: #if download could not be completed due to any exception or error, it will be displayed in a messagebox 
        messagebox.showerror('Error',e)

def download144p():
    url=url_entry.get()
    yt_path = dirpath_lab.cget("text") #getting the location where the video needs to be downloaded
    
    try: #downloading the video of selected resolution
        root.title('Downloading the youtube video...')
        ys=YouTube(url).streams.filter(resolution="144p") #downloading in 144p
        yt_video= ys.first().download()#downloading
        shutil.move(yt_video,yt_path) #moving video to the required path selected by user
        root.title('VIDEO Download Completed!!')
        messagebox.showinfo('DOWNLOADED','Youtube Video Downloaded!!') #messagebox for confirmation of download
    except Exception as e: #if download could not be completed due to any exception or error, it will be displayed in a messagebox 
        messagebox.showerror('Error',e)
def download480p():
    url=url_entry.get()
    yt_path = dirpath_lab.cget("text") #getting the location where the video needs to be downloaded
    
    try: #downloading the video of selected resolution
        root.title('Downloading the youtube video...')
        ys=YouTube(url).streams.filter(resolution="480p") #downloading in 480p
        yt_video= ys.first().download()#downloading
        shutil.move(yt_video,yt_path) #moving video to the required path selected by user
        root.title('VIDEO Download Completed!!')
        messagebox.showinfo('DOWNLOADED','Youtube Video Downloaded!!')#messagebox for confirmation of download
    except Exception as e: #if download could not be completed due to any exception or error, it will be displayed in a messagebox 
        messagebox.showerror('Error',e)

#Setting up Tkinter
root = Tk()
root.title('YOUTUBE VIDEO DOWNLOADERR')
img = PhotoImage(file="Internship_Task-2_youtube_icon.png")
root.iconphoto(False,img)
root.geometry('1200x1200')
#Using canvas
canvas = Canvas(root, width=700, height=700, bg='tan')
canvas.pack()
#Creating borders through canvas create_line function
canvas.create_line(0, 0, 700, 0, fill="black",width = 15)
canvas.create_line(0, 700, 700,700, fill="black",width = 15)
canvas.create_line(0, 0, 0, 700, fill="black",width = 15)
canvas.create_line(700, 0, 700, 700, fill="black",width = 15)
canvas.create_rectangle(350, 90, 350, 90, fill="red",width = 15)
#Placing youtube image using canvas create_image function
youtube_image= PhotoImage(file='Internship_Task-2_yt_1200.png')
youtube_image= youtube_image.subsample(2,2)  #resizing the image 
#Creating various download buttons
download_buttton=Button(root,text="DOWNLOAD VIDEO IN HIGHEST QUALITY",padx=30,pady=8,fg='white',bg='black',borderwidth=3, 
command=download_highestres)
canvas.create_window(250,400,window=download_buttton) #placing tkinter widget(here download button) in canvas using 
                                                       # canvas.create_window function

download_buttton360p=Button(root,text="DOWNLOAD VIDEO in 360p QUALITY",padx=25,pady=8,fg='white',bg='black',borderwidth=3, 
command=download360p)
canvas.create_window(250,450,window=download_buttton360p)#placing tkinter widget(here download button) in canvas using 
                                                       # canvas.create_window function

download_buttton480p=Button(root,text="DOWNLOAD VIDEO in 480p QUALITY",padx=27,pady=8,fg='white',bg='black',borderwidth=3, 
command=download480p)
canvas.create_window(250,500,window=download_buttton480p) #placing tkinter widget(here download button) in canvas using 
                                                       # canvas.create_window function

download_buttton240p=Button(root,text="DOWNLOAD VIDEO in 240p QUALITY",padx=23,pady=8,fg='white',bg='black',borderwidth=3, 
command=download240p)
canvas.create_window(250,550,window=download_buttton240p) #placing tkinter widget(here download button) in canvas using 
                                                       # canvas.create_window function

download_buttton144p=Button(root,text="DOWNLOAD VIDEO in 144p QUALITY",padx=20,pady=8,fg='white',bg='black',borderwidth=3, 
command=download144p)
canvas.create_window(250,600,window=download_buttton144p) #placing tkinter widget(here download button) in canvas using 
                                                       # canvas.create_window function

resetBtn= Button(root, text='Reset', font=7, fg='grey19',
                   command=reset_urlandlocation).place(relx=0.6, rely=0.75)
canvas.create_image(350,90,image=youtube_image) #using create_image function

select_btn = Button(root,text="BROWSE PATH",padx=10,fg='white',bg='black',command=browse_button)
canvas.create_window(350,315,window=select_btn)#placing tkinter widget(here download button) in canvas using 
                                                       # canvas.create_window function

dirpath_lab = Label(root,text='SELECT PATH TO DOWNLOAD :',font=('Times New Roman',9),fg='navy',bg='tan')
canvas.create_window(350,285,window=dirpath_lab)#placing tkinter widget(here label widget) in canvas using 
                                                       # canvas.create_window function

url_entry = Entry(root,width=50)
canvas.create_window(350,240,window=url_entry) #placing tkinter widget(here entry widget) in canvas using 
                                                       # canvas.create_window function

url_label=Label(root, text='Enter the Youtube link or url :', font=("Times New Roman", 13),fg='black',bg='tan')
canvas.create_window(350,215,window=url_label)#placing tkinter widget(here label widget) in canvas using 
                                               # canvas.create_window function

root.mainloop()
