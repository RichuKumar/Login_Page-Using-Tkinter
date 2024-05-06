import tkinter as tk
from PIL import Image, ImageTk
import tkinter.messagebox as mbox

class LoginWindow():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Login Page")
        self.root.geometry("1199x600+150+100")

        #Adding Background
        photo_path = "Photo/gradient.jpg"
        photo_pil = Image.open(photo_path)
        photo_pil_resized = photo_pil.resize((1199, 600))
        self.photo_pil = ImageTk.PhotoImage(photo_pil_resized)
        self.label = tk.Label(self.root, image=self.photo_pil)
        self.label.pack()

        #Adding Frame
        frame = tk.Frame(self.root, bg="thistle3")
        frame.place(x=350, y=100, width=550,height=400)

        #adding text inside the frame
        self.lable = (tk.Label(frame, text="Login", bg="thistle3",font=("Imapct", 30,"bold"), fg="Blue2")
                      .place(x=30,y=30))
        self.sublable = (tk.Label(frame, text="Member Login Area", bg="thistle3", font=("Ariel", 15), fg="Black")
                         .place(x=30, y=90))

        #username and password
        subtitle_username = tk.Label(frame, text="Username" , font=("Times New Roman", 15), fg="Black",bg="thistle3",)
        subtitle_username.place(x=50, y=140)
        self.Display_username = tk.Entry(frame, font=("Times New Roman", 15), fg="Black", width=20, bg="gray95")
        self.Display_username.place(x=50, y=170)
        subtitle_password = tk.Label(frame, text="Password", font=("Times New Roman", 15), fg="Black", bg="thistle3", )
        subtitle_password.place(x=50, y=220)
        self.Display_password = tk.Entry(frame, font=("Times New Roman", 15), fg="Black", width=20, bg="gray95")
        self.Display_password.place(x=50, y=250)

        #creating a button
        forget_button = tk.Button(frame, text="Forgot Password ?", bd=0,font=("Times New Roman", 10), fg="blue2",cursor="hand2", bg="thistle3")
        forget_button.place(x=50, y=300)
        Submit_button = tk.Button(frame, text="Submit", font=("Ariel", 12,"bold"), fg="white",
                                  cursor="hand2", bg="blue2",command=self.Info)
        Submit_button.place(x=250, y=330)

    def Info(self):
        Username = self.Display_username.get()
        Password = self.Display_password.get()

        if Username == "" or Password == "":
            mbox.showerror("Error", "Please enter username and password.", parent=self.root)
        elif Username != "Richi" or Password != "1234":
            mbox.showerror("Error", "Please check your username or password.", parent=self.root)
        else:
            mbox.showinfo("Loggined", "Login Successful")


login = LoginWindow()
login.root.mainloop()