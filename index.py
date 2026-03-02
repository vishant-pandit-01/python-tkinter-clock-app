# import datetime
# import time

# while True:
#     now = datetime.datetime.now()
#                  #for 24 hour format
#     # print(now.strftime("%H:%M:%S"), end="\r")       

#                 #for 12 hour format
#     print(now.strftime("%I:%M:%S"), end="\r")        
    
#     time.sleep(1)



# from tkinter import *
# import datetime

# root = Tk()
# root.geometry("400x400")
# root.config(bg="black")
# root.title("Digital Clock")
# design=Frame(root,background="black",highlightbackground="red",highlightthickness=2)
# design.place(relx="0.5",rely="0.5",anchor="center",height="380",width="380")


# def clock():
#     now = datetime.datetime.now()
#     current_time = now.strftime("%I:%M:%S:%p")
#     current_date=now.strftime("%A")

#     label.config(text=current_time)
#     label.after(1000, clock)  # update every 1 second 

#     label_date.config(text=current_date)

# label = Label(design, bg="black", fg="white",font=("arial",30),anchor="center")
# label.grid(row=1,column=0)
# label_date = Label(design, bg="black", fg="white",font=("arial"))
# label_date.grid(row=2,column=0)
# clock()  

# root.mainloop() 




# from tkinter import *
# import datetime

# root = Tk()
# root.geometry("400x400")
# root.config(bg="black")
# root.title("Digital Clock")

# design = Frame(root, bg="black", highlightbackground="red", highlightthickness=2)
# design.place(relx=0.5, rely=0.5, anchor="center", height=380, width=380)

# def clock():
#     now = datetime.datetime.now()
#     current_time = now.strftime("%I:%M:%S %p")   # better format
#     current_day = now.strftime("%A")
#     current_date = now.strftime("%d %B %Y")

#     label_time.config(text=current_time)
#     label_day.config(text=current_day)
#     label_date.config(text=current_date)

#     label_time.after(1000, clock)  # update every 1 second

# label_time = Label(design, bg="black", fg="cyan",
#                    font=("Arial", 32, "bold"))
# label_time.grid(row=0, column=0, pady=20)

# label_day = Label(design, bg="black", fg="white",
#                   font=("Arial", 18))
# label_day.grid(row=1, column=0)

# label_date = Label(design, bg="black", fg="white",
#                    font=("Arial", 16))
# label_date.grid(row=2, column=0)

# clock()
# root.mainloop()


# from tkinter import *
# import datetime

# root = Tk()
# root.geometry("400x400")
# root.config(bg="black")
# root.title("Digital Clock")

# design=Frame(bg="black",highlightbackground="red",highlightthickness=2)
# design.place(relx=0.5,rely=0.5,anchor="center",height="350",width="350")

# def clock():
#     now = datetime.datetime.now()
#     current_time = now.strftime("%I:%M:%S %p")
#     label.config(text=current_time)
#     label.after(1000, clock)

# label = Label(design, bg="black", fg="cyan",
#               font=("Arial", 35, "bold"),foreground="white")

# # Perfect center
# label.place(relx=0.5, rely=0.5, anchor="center")

# clock()
# root.mainloop()



# from tkinter import *
# import datetime

# root = Tk()
# root.geometry("400x400")
# root.config(bg="black")
# root.title("Digital Clock")

# design = Frame(root, bg="black",highlightbackground="cyan",
#                highlightthickness=2)
# design.place(relx=0.5, rely=0.5, anchor="center",
#              height=350, width=350)

# colors = ["red", "yellow", "cyan", "lime", "orange", "magenta"]
# color_index = 0

# def animate_border():
#     global color_index
#     design.config(highlightbackground=colors[color_index])
#     color_index = (color_index + 1) % len(colors)
#     root.after(500, animate_border)   # change every 0.5 sec

# def clock():
#     now = datetime.datetime.now()
#     current_time = now.strftime("%I:%M:%S %p")
#     label.config(text=current_time)
#     label.after(1000, clock)

# label = Label(design, bg="black", fg="cyan",
#               font=("Arial", 35, "bold"))
# label.place(relx=0.5, rely=0.5, anchor="center")

# clock()
# # animate_border()
# root.mainloop()


from tkinter import *
import datetime

root = Tk()
root.geometry("400x400")
root.config(bg="black")
root.title("Digital Clock")

design = Frame(root, bg="black",highlightbackground="red",
               highlightthickness=2)
design.place(relx=0.5, rely=0.5, anchor="center",
             height=350, width=350)
def clock():
    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M:%S %p")
    current_date = now.strftime("%A\n%d %B %Y")
    label.config(text=current_time + "\n" + current_date)
    label.after(1000, clock)

label = Label(design, bg="black", fg="cyan",
              font=("Arial", 35, "bold"))
label.place(relx=0.5, rely=0.5, anchor="center")

clock()
root.mainloop()
