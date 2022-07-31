#UNIcompiler Internship Task-3

#In this task we have to make a mp3 music player through
# which users can play their MP3 files and other digital 
# audio files without having to purchase a physical MP3 Player.

import pygame #importing the pygame module
import tkinter #importing tkinter for GUI
from tkinter import *
from tkinter.filedialog import askdirectory
import os

#setting up tkinter
root = tkinter.Tk() 
root.title("Music Player") #giving title
root.geometry('1200x1200') #defining size
root.configure(bg= "#0f1a2b") #giving background 

# setting up icon
img = PhotoImage(file="Internship_Task-3_music-logo.png")
root.iconphoto(False,img)

#creating a heading that will show the name of current song
heading = tkinter.StringVar()
heading.set("Select the song to play")

#selecting folder which has songs 
#browsing
os.chdir(askdirectory())
songlist = os.listdir()

#creating a listbox which will contain list of songs
root_listbox = tkinter.Listbox(root,font="Helvetica 12 bold",width=120,height
=30,bg="tan",fg="black",selectmode=tkinter.SINGLE) 

#inserting songs from the songlist to the listbox
for item in songlist:
    root_listbox.insert(0,item)

#Initialising the pygame module
pygame.init()
pygame.mixer.init()

#setting a variable to update the status of song 
songstatus=StringVar()
songstatus.set("Choosing the song")

#defining various functions for play,pause,resume,stop etc.

#function for playing the song
def playsong():
    pygame.mixer.music.load(root_listbox.get(tkinter.ACTIVE)) #loading the 
                                                            #current song
    name = root_listbox.get(tkinter.ACTIVE) #getting the name of the song
    heading.set(name) #setting the heading as the name of the song
    songstatus.set("Playing") #Updating the song status to Playing
    pygame.mixer.music.play() #playing the song

#function for pausing the song
def pausesong():
    songstatus.set("Paused") #Updating the song status to Paused
    pygame.mixer.music.pause() #pausing the song

#function for resuming the song
def resumesong():
    songstatus.set("Resumed") #Updating the song status to Resumed
    pygame.mixer.music.unpause() #unpausing or resuming the song

#function for stopping the song
def stopsong(): 
    songstatus.set("Stopped") #Updating the song status to Stopped
    heading.set("Select the song to play") #Setting heading to default
    pygame.mixer.music.stop() #Stopping the song

#function for playing the next song in list
def Nextsong():
    
    next_song=root_listbox.curselection() # getting the selected song index
    next_song=next_song[0]+1 #getting the index of the next song
    temp=root_listbox.get(next_song) #getting the next song

    pygame.mixer.music.load(temp) #loading the next song
    pygame.mixer.music.play() #playing that next song

    heading.set(temp)#setting the heading to the name of the next song
    songstatus.set("Playing") #updating song status to playing
    root_listbox.selection_clear(0,END)
    #activate newsong
    root_listbox.activate(next_song)
    #set the next song
    root_listbox.selection_set(next_song)

#function for playing the previous song in list
def Previoussong():

    previous_song=root_listbox.curselection()#getting the selected song index
    previous_song=previous_song[0]-1 #getting the index of the previous song
    temp2=root_listbox.get(previous_song) #getting the previous song

    pygame.mixer.music.load(temp2)#loading the next song
    pygame.mixer.music.play() #playing that previous song

    heading.set(temp2)#setting the heading to the name of the next song
    songstatus.set("Playing")#updating song status to playing
    root_listbox.selection_clear(0,END)
    #activating new song
    root_listbox.activate(previous_song)
    #setting the next song
    root_listbox.selection_set(previous_song)

#defining the label for heading i.e name of the song currently playing
text = tkinter.Label(root,font="Helvetica",textvariable=heading).grid(row=0,
columnspan=6)

#defining the label for songstatus i.e playing,stopped,paused etc.
text1 = tkinter.Label(root,font="Helvetica",textvariable=songstatus).grid(row
=1,columnspan=6) 

#making the listbox size same as that of grid of columnspan 6
root_listbox.grid(columnspan=6)

#creating various buttons i.e play,pause,resume,stop etc.

#Creating play button and placing the button in grid of row 3 column 0
play_btn = tkinter.Button(root,width=7,height=1,font="Helvetica",text="Play",
command=playsong,bg="lightgreen").grid(row=3,column=0)

#Creating pause button and placing the button in grid of row 3 column 1
pause_btn = tkinter.Button(root, width=7, height=1, font="Helvetica",text
="Pause", command=pausesong, bg="lightblue", fg="black").grid(row=3,column=1)

#Creating resume button and placing the button in grid of row 3 column 2
resume_btn = tkinter.Button(root, width=9, height=1, font="Helvetica", text
="Resume", command=resumesong, bg="lightpink", fg="black").grid(row=3,column=2)

#Creating stop button and placing the button in grid of row 3 column 3
stop_btn = tkinter.Button(root, width=11, height=1, font="Helvetica", text
="Stop", command=stopsong, bg="lightgreen", fg="black").grid(row=3,column=3)

#Creating next song button and placing the button in grid of row 3 column 4
nsong_btn = tkinter.Button(root, width=11, height=1, font="Helvetica",text=
"Next Song",command=Nextsong,bg="mistyrose2",fg="black").grid(row=3,column=4)

#Creating previous song button and placing the button in grid of 
# row 3 column 5
psong_btn = tkinter.Button(root,width=11,height=1,font="Helvetica",text=
"Previous Song",command=Previoussong,bg="lightyellow",
fg="black").grid(row=3,column=5)

root.mainloop()