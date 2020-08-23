from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk  # Normal Tkinter.* widgets are not themed!
from ttkthemes import ThemedTk
from  tkinter import filedialog


root = ThemedTk(theme="radiance")

root.title("MCQ")
root.iconbitmap('F:\python\draft\images\exams.ico')
#root.geometry("400x400")


def q_open():
    top3 = Toplevel()
    top3.filename = filedialog.askopenfilename(initialdir="F:/python/draft/images/", title="select a file", filetypes=(("png files", "*.png"), ("all files", "*.*")))
    q_label = Label(top3, text = "The question paper will be attached here").grid(padx = 100,pady=100)


def signup():
    top2 = Toplevel()
    ttk.Label(top2, text="Enter Username").grid(row=10, column=10, padx=2, pady=2)
    e1 = ttk.Entry(top2, width=50).grid(row=11, column=10, padx=100, pady=10)
    ttk.Label(top2, text="Enter Password").grid(row=12, column=10, padx=2, pady=2)
    e2 = ttk.Entry(top2, width=50).grid(row=13, column=10, padx=100, pady=10)
    ttk.Label(top2, text="Confirm Password").grid(row=14, column=10, padx=2, pady=2)
    e3 = ttk.Entry(top2, width=50).grid(row=15, column=10, padx=100, pady=10)
    ttk.Button(top2, text="Sign Up", command= top2.destroy).grid(row=16, column=10, padx=10, pady=10)


def selected():
  if clicked.get()=="Student":
      top = Toplevel()
      # Column 2 starts from here >>
      r = IntVar()
      ttk.Label(top, text="Answer no. 1").grid(padx=50, pady=5, row=1, column=1)
      ttk.Radiobutton(top, text="A", variable=r, value=1).grid(row=2, column=1)
      ttk.Radiobutton(top, text="B", variable=r, value=2).grid(row=3, column=1)
      ttk.Radiobutton(top, text="C", variable=r, value=3).grid(row=4, column=1)
      ttk.Radiobutton(top, text="D", variable=r, value=4).grid(row=5, column=1)
      ttk.Label(top, text="Answer no. 2").grid(padx=25, pady=5, row=6, column=1)
      r2 = IntVar()
      ttk.Radiobutton(top, text="A", variable=r2, value=1).grid(row=7, column=1)
      ttk.Radiobutton(top, text="B", variable=r2, value=2).grid(row=8, column=1)
      ttk.Radiobutton(top, text="C", variable=r2, value=3).grid(row=9, column=1)
      ttk.Radiobutton(top, text="D", variable=r2, value=4).grid(row=10, column=1)
      ttk.Label(top, text="Answer no. 3").grid(padx=25, pady=5, row=11, column=1)
      r3 = IntVar()
      ttk.Radiobutton(top, text="A", variable=r3, value=1).grid(row=12, column=1)
      ttk.Radiobutton(top, text="B", variable=r3, value=2).grid(row=13, column=1)
      ttk.Radiobutton(top, text="C", variable=r3, value=3).grid(row=14, column=1)
      ttk.Radiobutton(top, text="D", variable=r3, value=4).grid(row=15, column=1)
      r4 = IntVar()
      ttk.Label(top, text="Answer no. 4").grid(padx=25, pady=5, row=16, column=1)
      ttk.Radiobutton(top, text="A", variable=r4, value=1).grid(row=17, column=1)
      ttk.Radiobutton(top, text="B", variable=r4, value=2).grid(row=18, column=1)
      ttk.Radiobutton(top, text="C", variable=r4, value=3).grid(row=19, column=1)
      ttk.Radiobutton(top, text="D", variable=r4, value=4).grid(row=20, column=1)
      r5 = IntVar()
      ttk.Label(top, text="Answer no. 5").grid(padx=25, pady=5, row=21, column=1)
      ttk.Radiobutton(top, text="A", variable=r5, value=1).grid(row=22, column=1)
      ttk.Radiobutton(top, text="B", variable=r5, value=2).grid(row=23, column=1)
      ttk.Radiobutton(top, text="C", variable=r5, value=3).grid(row=24, column=1)
      ttk.Radiobutton(top, text="D", variable=r5, value=4).grid(row=25, column=1)

      # Column 2 starts from here >>

      r6 = IntVar()
      ttk.Label(top, text="Answer no. 6").grid(padx=25, pady=5, row=1, column=2)
      ttk.Radiobutton(top, text="A", variable=r6, value=1).grid(row=2, column=2)
      ttk.Radiobutton(top, text="B", variable=r6, value=2).grid(row=3, column=2)
      ttk.Radiobutton(top, text="C", variable=r6, value=3).grid(row=4, column=2)
      ttk.Radiobutton(top, text="D", variable=r6, value=4).grid(row=5, column=2)
      r7 = IntVar()
      ttk.Label(top, text="Answer no. 7").grid(padx=25, pady=5, row=6, column=2)
      ttk.Radiobutton(top, text="A", variable=r7, value=1).grid(row=7, column=2)
      ttk.Radiobutton(top, text="B", variable=r7, value=2).grid(row=8, column=2)
      ttk.Radiobutton(top, text="C", variable=r7, value=3).grid(row=9, column=2)
      ttk.Radiobutton(top, text="D", variable=r7, value=4).grid(row=10, column=2)
      r8 = IntVar()
      ttk.Label(top, text="Answer no. 8").grid(padx=25, pady=5, row=11, column=2)
      ttk.Radiobutton(top, text="A", variable=r8, value=1).grid(row=12, column=2)
      ttk.Radiobutton(top, text="B", variable=r8, value=2).grid(row=13, column=2)
      ttk.Radiobutton(top, text="C", variable=r8, value=3).grid(row=14, column=2)
      ttk.Radiobutton(top, text="D", variable=r8, value=4).grid(row=15, column=2)
      r9 = IntVar()
      ttk.Label(top, text="Answer no. 9").grid(padx=25, pady=5, row=16, column=2)
      ttk.Radiobutton(top, text="A", variable=r9, value=1).grid(row=17, column=2)
      ttk.Radiobutton(top, text="B", variable=r9, value=2).grid(row=18, column=2)
      ttk.Radiobutton(top, text="C", variable=r9, value=3).grid(row=19, column=2)
      ttk.Radiobutton(top, text="D", variable=r9, value=4).grid(row=20, column=2)
      r10 = IntVar()
      ttk.Label(top, text="Answer no. 10").grid(padx=25, pady=5, row=21, column=2)
      ttk.Radiobutton(top, text="A", variable=r10, value=1).grid(row=22, column=2)
      ttk.Radiobutton(top, text="B", variable=r10, value=2).grid(row=23, column=2)
      ttk.Radiobutton(top, text="C", variable=r10, value=3).grid(row=24, column=2)
      ttk.Radiobutton(top, text="D", variable=r10, value=4).grid(row=25, column=2)
      ttk.Button(top, text="Submit your Answer", command=top.destroy).grid(row=26, column=1, padx=50, pady=30)
      # timer_img = ImageTk,PhotoImage(Image.open("F:\python\draft\images\timer.png"))
      # timer_label = Label(top, image=timer_img)
      # timer_label.grid(row=1,column=3)

      timer_text = Label(top, text="Time remaining: ").grid(row=1, column=3, padx=30, pady=20)
      time_text = Label(top, text="[ 00:00:00 ]").grid(row=2, column=3)
      q_button = ttk.Button(top, text="Open question paper", command=q_open).grid(row=3, column=3, padx=30)

  elif clicked.get()=='teacher':
      teacher_top = Toplevel()
      teacher_top.geometry("400x400")


  #timer option starts here
  def set_time():
      global t
      t=0
      t = t+int(t_entry.get())
      return t

  def countdown():
      global t
      if t>0:
          t_label.config(text = t)
          t = t-1
          t_label.after(1000,countdown)

      elif t==0:
          t_label.config(text="Stop Writing")


  ttk.Label(teacher_top,text = "Time Remaining").grid(row=0,column=1,pady=15)
  t_label = ttk.Label(teacher_top,font = "times 20")
  t_label.grid(row=2,column = 1)

  times = StringVar()
  Label(teacher_top, text="Set time here").grid(row=3,column=1,pady=5)
  t_entry = ttk.Entry(teacher_top,textvariable = times)
  t_entry.grid(row=4,column=1,padx=140,pady=20)
  set_timer = ttk.Button(teacher_top,text = "Set",command = set_time).grid(row = 5,column = 1,pady=4)
  start_timer = ttk.Button(teacher_top,text = "Start Exam",command = countdown).grid(row = 6,column=1,pady=4)




#Homemenu
clicked = StringVar()
#clicked.set("Logging in as")
options = [ "Logging in as","Student", "teacher"]
ttk.OptionMenu(root, clicked,*options).grid(row=9,column=10,padx=50, pady=50)
ttk.Label(root, text = "Enter Username").grid(row=10,column=10,padx=2, pady=2)
e1 = ttk.Entry(root,width=50).grid(row=11,column=10,padx=100, pady=10)
ttk.Label(root, text = "Enter Password").grid(row=12,column=10,padx=2, pady=2)
e2 = ttk.Entry(root,width=50).grid(row=13,column=10,padx=100, pady=10)
login_btn = ttk.Button(root, text = "Log In", command=selected).grid(row=15,column=10,padx=10, pady=10)
#sign up option
ttk.Label(root, text = "Haven't login yet? Sign up here").grid(row=16,column=10,padx=5, pady=5)
ttk.Button(root, text = "Sign Up",command = signup).grid(row=17,column=10,padx=5, pady=5)

root.mainloop()