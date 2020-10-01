import tkinter as tk
from PIL import ImageTk, Image
import os
from bs4 import BeautifulSoup
import urllib.request

def score():
    T.insert(tk.END,ls)

def clear():
    T.delete(1.0,tk.END)
score_page='http://static.cricinfo.com/rss/livescores.xml'

page=urllib.request.urlopen(score_page)

soup = BeautifulSoup(page,'html.parser')

result =soup.find_all('description')

ls=[]

for match in result:
    ls.append(match.get_text())
     
root =tk.Toplevel()
root.geometry('810x540')

img=ImageTk.PhotoImage(Image.open("ipl.jpg"))

panel =tk.Label(root,image=img)
panel.place(x=0,y=0)

T=tk.Text(root)
T.place(x=30,y=250,height=250,width=300)

l=tk.Label(root,text="Live Cricket Score By Espn")
l.place(x=30,y=400,height=100,width=300)

b1=tk.Button(root,text="Score",bg="blue",fg="white",command=score)
b1.place(x=650,y=300,height=60,width=150)

b2=tk.Button(root,text="Clear",bg="blue",fg="white",command=clear)
b2.place(x=650,y=400,height=60,width=150)

root.mainloop()




