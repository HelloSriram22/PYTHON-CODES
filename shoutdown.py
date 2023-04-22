# from tkinter import
# import os

# def restart():
#     os.system("shutdown/r/t1")

# def restart_time():
#     os.system("shutdown/r/t20")

# def logout():
#     os.system("shutdown-1")

# def shutdown():
#     os.system("shutdown/s/t1")

# st = Tk()
# st.title("shutdown app")
# st.geometry("500x500")
# st.config(bg="red")

# r_button=Button(st,text="restart",font=("time new roman",20,'bold'),relif="raised",cursor="plus",command=restart)
# r_button.place(x=150,y=60,height=50,width=200)

# rt_button=Button(st,text="restart time",font=("times new roman",20,"bold"),relief="raised",cursor="plus",command=restart_time)

# ig_button=Button(st,text="log-out",font=("time new roman",20,"bold"),relif="raised",cursor="plus",command=logout)
# ig_button.place(x=150,y=270,height=50,width=200)

# st_button = Button(st, text="shutdown", font=("times new roman", 20, "bold"), relief="raised", cursor="plus", command=shutdown)
# st_button.place(x=150,y=370,height=50,width=200)

# st.mainloop()

from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")
    
def restart_time():
    os.system("shutdown /r /t 20")
    
def logout():
    os.system("shutdown /l")
    
def shutdown():
    os.system("shutdown /s /t 1")
    
st=Tk()
st.title("shutdown app")
st.geometry("500x500")
st.config(bg="red")

r_button=Button(st,text="restart",font=("times new roman",20,'bold'),relief="raised",cursor="plus",command=restart)
r_button.place(x=150,y=60,height=50,width=200)

rt_button=Button(st,text="restart time",font=("times new roman",20,"bold"),relief="raised",cursor="plus",command=restart_time)
rt_button.place(x=150,y=170,height=50,width=200)

ig_button=Button(st,text="log-out",font=("times new roman",20,"bold"),relief="raised",cursor="plus",command=logout)
ig_button.place(x=150,y=270,height=50,width=200)

st_button=Button(st,text="shutdown",font=("times new roman",20,"bold"),relief="raised",cursor="plus",command=shutdown)
st_button.place(x=150,y=370,height=50,width=200)

st.mainloop()
              