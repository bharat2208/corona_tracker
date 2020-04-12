import requests
import plyer
import datetime
import bs4
from tkinter import  *
import tkinter as tk
from PIL import ImageTk,Image
from tkinter import messagebox



### GUI
root=Tk()
def get_html_data(url):
    data=requests.get(url)
    return data
url = "https://www.mohfw.gov.in/"
html_data=get_html_data(url)
bs=bs4.BeautifulSoup(html_data.text,'html.parser')


    ## ACTIVE CASES
count_Active=bs.find("li",class_="bg-blue").find_all("strong")
for actives in count_Active:
    actives.get_text()
string_Active = bs.find("li", class_="bg-blue").find_all("span")
for text in string_Active:
    text.get_text()
active_details=(str(text.get_text())+":"+str(actives.get_text()))
##DISCHARGED CASES
count_discharged=bs.find("li",class_="bg-green").find_all("strong")
for discharge in count_discharged:
        discharge.get_text()
string_discharged = bs.find("li", class_="bg-green").find_all("span",class_="mob-hide")
for text1 in string_discharged:
    text1.get_text()

cured_details=(str(text1.get_text()) + ":" + str(discharge.get_text()))
    ##Deaths
count_deaths=bs.find("li",class_="bg-red").find_all("strong")
for deaths_counts in count_deaths:
    deaths_counts.get_text()
string_deaths=bs.find("li",class_="bg-red").find_all("span")
for text2 in string_deaths:
    text2.get_text()
deaths_details=(str(text2.get_text())+":"+deaths_counts.get_text())
    ##MIGRATED
count_migrated = bs.find("li", class_="bg-orange").find_all("strong")
for migrated in count_migrated:
    migrated.get_text()
string_migrated = bs.find("li", class_="bg-orange").find_all("span")
for text3 in string_migrated:
    text3.get_text()
migrated_details=(str(text3.get_text()) + ":" + migrated.get_text())
all_details=active_details+"\n"+cured_details+"\n"+deaths_details+"\n"+migrated_details



root.geometry("2000x1000")
root.title("CORONA DATA TRACKER-INDIA")
f=("poppins",30,"bold")
tracker = ImageTk.PhotoImage(Image.open("corona_tracker.png"))
panel=Label(root,image=tracker,bg="gray",width=100)
panel.pack(side="top",fill=X)

canvas_active=Canvas(root,bg="light blue")
active= ImageTk.PhotoImage(Image.open("active.png"))
active_lab=Label(canvas_active,image=active,width=50,bg="light blue")
canvas_active.create_window(79,40,window=active_lab)
label_active=Label(canvas_active,text=actives.get_text(),font=f,bg="light blue")
canvas_active.create_window(79,100,window=label_active)
label_active_count=Label(canvas_active,text=text.get_text(),font=("poppins",20,"bold"),bg="light blue")
canvas_active.create_window(94,140,window=label_active_count)
canvas_active.place(x=30,y=170,height=180,width=190)

canvas_cured=Canvas(root,bg="light green")
cured= ImageTk.PhotoImage(Image.open("cured.png"))
cured_lab=Label(canvas_cured,image=cured,width=50,bg="light green")
canvas_cured.create_window(120,40,window=cured_lab)
label_cured_count=Label(canvas_cured,text=discharge.get_text(),font=f,bg="light green")
canvas_cured.create_window(120,100,window=label_cured_count)
label_cured=Label(canvas_cured,text=text1.get_text(),font=("poppins",20,"bold"),bg="light green")
canvas_cured.create_window(140,140,window=label_cured)
canvas_cured.place(x=330,y=170,height=180,width=278)

canvas_deaths=Canvas(root,bg="light coral")
deaths= ImageTk.PhotoImage(Image.open("deaths.png"))
deaths_lab=Label(canvas_deaths,image=deaths,width=50,bg="light coral")
canvas_deaths.create_window(79,40,window=deaths_lab)

label_deaths_count=Label(canvas_deaths,text=deaths_counts.get_text(),font=f,bg="light coral")
canvas_deaths.create_window(79,100,window=label_deaths_count)
label_deaths=Label(canvas_deaths,text=text2.get_text(),font=("poppins",20,"bold"),bg="light coral")
canvas_deaths.create_window(79,140,window=label_deaths)
canvas_deaths.place(x=770,y=170,height=180,width=170)

canvas_migrated=Canvas(root,bg="tan1")
migrated_img= ImageTk.PhotoImage(Image.open("migrate.png"))
migrated_lab=Label(canvas_migrated,image=migrated_img,width=50,bg="tan1")
canvas_migrated.create_window(79,40,window=migrated_lab)

label_migrated_count=Label(canvas_migrated,text=migrated.get_text(),font=f,bg="tan1")
canvas_migrated.create_window(79,100,window=label_migrated_count)
label_migrated=Label(canvas_migrated,text=text3.get_text(),font=("poppins",20,"bold"),bg="tan1")
canvas_migrated.create_window(79,140,window=label_migrated)

canvas_migrated.place(x=1140,y=170,height=180,width=170)
#mainlabel=Label(root,text=get_corona_detail(),font=f)
#mainlabel.pack()
def refresh():
    new_active=actives.get_text()
    label_active['text']=new_active
    new_cured=discharge.get_text()
    label_cured_count['text']=new_cured
    new_deaths=deaths_counts.get_text()
    label_deaths_count['text']=new_deaths
    new_migrated=migrated.get_text()
    label_migrated_count['text']=new_migrated
    messagebox.showinfo("UPDATE","STATS REFRESHED")
   # mainlabel['text']=newdata
refresh_but=Button(root,text="Refresh",command=refresh,font=("poppins",20,"bold"),bg="purple")
refresh_but.place(x=630,y=370)
bg_hex="#468bcc"
canvas_safety=Canvas(root,bg=bg_hex)
safety = ImageTk.PhotoImage(Image.open("corona_safety.png"))
safety_lab=Label(canvas_safety,image=safety,width=700,height=280,bg=bg_hex)
canvas_safety.create_window(700,150,window=safety_lab)

canvas_safety.place(x=0,y=420,width=1357,height=300)
root.mainloop()
