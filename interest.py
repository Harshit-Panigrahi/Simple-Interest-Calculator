from tkinter import *

window = Tk()

window.title("Simple Interest Calculator")
window.geometry("400x450")
window.resizable(0, 0)
window.configure(bg="#336699")

app_title = Label(
  window,
  text="Simple Interest Calculator",
  bg="#aaccee",
  fg="#336699",
  font="Helvetica 18 bold"
)
app_title.place(relwidth=1)

p_label = Label(
  window,
  text="Principal (₹):",
  bg="#336699",
  fg="#aaccee",
  font="Helvetica 16 bold"
)
p_label.place(relx=0.07, rely=0.15)

r_label = Label(
  window,
  text="Rate (%pa):",
  bg="#336699",
  fg="#aaccee",
  font="Helvetica 16 bold"
)
r_label.place(relx=0.07, rely=0.3)

t_label = Label(
  window,
  text="Time (yrs):",
  bg="#336699",
  fg="#aaccee",
  font="Helvetica 16 bold"
)
t_label.place(relx=0.07, rely=0.45)

p_entry = Entry(window)
r_entry = Entry(window)
t_entry = Entry(window)
p_entry.place(relx=0.42, rely=0.16, relwidth=0.4, height=25)
r_entry.place(relx=0.42, rely=0.31, relwidth=0.4, height=25)
t_entry.place(relx=0.42, rely=0.46, relwidth=0.4, height=25)

calc_btn = Button(
  window,
  text="Calculate",
  font="Helvetica 13 bold",
  bg="#aaccee",
  fg="#336699",
  command=lambda: calc_ci()
)
calc_btn.place(relx=0.5, rely=0.62, anchor=CENTER)

res_label = Label(
  window,
  text="The result will appear here.",
  bg="#336699",
  fg="#aaccee",
  font="Helvetica 16 bold" 
)
res_label.place(relx=0.5, rely=0.75, anchor=CENTER)

def calc_ci():
  try:
    p = float(p_entry.get())
    r = float(r_entry.get())
    t = float(t_entry.get())
    i = (p*r*t)/100
    a = i+p
    res_label.config(
      text=f"Interest: ₹{i},\nAmount:₹{a}",
    )
  except:
    res_label.config(
      text="An error occured. Try again.",
    )

window.mainloop()
