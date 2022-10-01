# importing required module
from tkinter import *
from gtts import gTTS
 
# this module helps to
# play the converted audio 
import os
 
# create tkinter window
root = Tk()
 
# styling the frame which helps to 
# make our background stylish
frame1 = Frame(root,
               bg = "lightPink",
               height = "150")
 
# place the widget in gui window
frame1.pack(fill = X)
 
 
frame2 = Frame(root,
               bg = "lightgreen",
               height = "750")
frame2.pack(fill=X)
 
 
 
# styling the label which show the text 
# in our tkinter window
label = Label(frame1, text = "Text to Speech",
              font = "bold, 30",
              bg = "lightpink")
 
label.place(x = 180, y = 70)
 
 
 
# entry is used to enter the text 
entry = Entry(frame2, width = 45,
              bd = 4, font = 14)
 
entry.place(x = 130, y = 52)
entry.insert(0, "")
 
# define a function which can
# get text and convert into audio
def play():
 
    # Language in which you want to convert 
    language = "en"
 
 
 
   # Passing the text  and language, 
   # here we have  slow=False. Which tells 
   # the module that the converted audio should 
   # have a high speed 
 
    myobj = gTTS(text = entry.get(),
                lang = language,
                slow = False)
 
 
 
    # give the name as you want to 
    # save the audio
    myobj.save("convert.wav")
    os.system("convert.wav")
 
# cereate a button which holds
# our play function using command = play
btn = Button(frame2, text = "SUBMIT",
             width = "15", pady = 10,
             font = "bold, 15",
             command = play, bg='yellow')
 
btn.place(x = 250,
          y = 130)
 
# give a title 
root.title("text_to_speech_convertor")
 
 
 
# we can not change the size
# if you want you can change
root.geometry("650x550+350+200")
 
# start the gui
root.mainloop()