from tkinter import *
from PIL import Image, ImageTk
from subprocess import call

root = Tk()
root.title("Hotel Management System")
root.resizable(False, False)
root.geometry("1000x500+150+80")


def Cust():
    root.destroy()
    call(["python", "C_home.py"])

def Stuff():
    root.destroy()
    call(["python", "Stuff_log.py"])

def Admin():
    root.destroy()
    call(["python", "Admin_log.py"])


lbl_title = Label(root, text="Hotel Management System", font=("comic sans ms", 38, "bold"), bg="black", fg="gold", bd=2, relief=RIDGE)
lbl_title.place(x=0, y=0, width=1000, height=130)

main_frame = Frame(root, bd=2, relief=RIDGE)
main_frame.place(x=0, y=130, width=1000, height=370)

canv = Canvas(main_frame, width=1000, height=370)
canv.place(x=0, y=0)

img = ImageTk.PhotoImage(Image.open("d2.jpg"))
canv.create_image(0, 0, anchor=NW, image=img)
#canv.create_text(250, 240, text="Our Service:", font=("times new roman", 20, "bold"), fill="Yellow")

#canv.create_text(380, 300, text=".24-hour front desk\n.Daily housekeeping\n.Key card access\n.CCTV in common areas\n.WiFi available in all areas", font=("arial", 12, 'bold'), fill="white")

admin_btn = Button(main_frame, width=9, text="Admin", command=Admin, font=("times new roman", 15, "bold"), bg="black", fg="gold")
admin_btn.place(x=450, y=280)

stuff_btn = Button(main_frame, width=9, text="Receptionist", command=Stuff, font=("times new roman", 15, "bold"), bg="black", fg="gold")
stuff_btn.place(x=600, y=280)

cust_btn = Button(main_frame, width=9, text="Customer", command=Cust, font=("times new roman", 15, "bold"), bg="black", fg="gold")
cust_btn.place(x=750, y=280)


root.mainloop()
