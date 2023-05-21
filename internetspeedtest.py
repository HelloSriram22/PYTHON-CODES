# from tkinter import*
# import speedtest
# def speedcheck():
#     sp=speedtest.speedtest()
#     sp.get_servers()
#     down=str(round(sp.downlord()/(10**6),3))+"mbps"
#     up=str(round(sp.uplord()/(10**6),3))+"mbps"
#     lab_down.config(text=down)
#     lab_up.config(text=up)
# sp=tk()
# sp.title("internet speed test")
# sp.geometry("500*650")
# sp.config(bg="blue")

# lab=Label(sp,text="internet speed test",font=("time new roman",30,"bold"),bg=blue,"bold",fg="yellow")
# lab.place(x=60,y=40,height=50,width=380)

# lab=lebal(sp,text="downlord speed",font=("time new roman",30))
# lab.place(x=60,y=130,height=50,width=380)

# lab=Label(sp,text="00",font=("time new roman",30,"blue"))
# lab.place(x=60,y=200,height=50,width=380)

# lab=Label(sp,text="uplord speed",font=("times new roman",30,"bold"))
# lab.place(x=60,y=290,height=50,width=380)

# lab=Label(sp,text="00",font=("time new roman",30,"bold"))
# lab.place(x=60,y=360,height=50,width=380)

# botton=Button(sp,text="check speed ",font=("timenew roman",30,"bold"),relief=raise,bg="red",command=speedcheck)




from tkinter import *
import speedtest

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6), 3)) + "mbps"
    up = str(round(sp.upload()/(10**6), 3)) + "mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)

sp = Tk()
sp.title("internet speed test")
sp.geometry("500x650")
sp.config(bg="blue")

lab = Label(sp, text="internet speed test", font=("times new roman", 30, "bold"), bg="blue", fg="yellow")
lab.place(x=60, y=40, height=50, width=380)

lab_down = Label(sp, text="downlord speed", font=("times new roman", 30))
lab_down.place(x=60, y=130, height=50, width=380)

lab_down_val = Label(sp, text="00", font=("times new roman", 30, "blue"))
lab_down_val.place(x=60, y=200, height=50, width=380)

lab_up = Label(sp, text="uplord speed", font=("times new roman", 30, "bold"))
lab_up.place(x=60, y=290, height=50, width=380)

lab_up_val = Label(sp, text="00", font=("times new roman", 30, "bold"))
lab_up_val.place(x=60, y=360, height=50, width=380)

button = Button(sp, text="check speed", font=("times new roman", 30, "bold"), relief="raised", bg="red", command=speedcheck)
button.place(x=60, y=450, height=50, width=380)

sp.mainloop()
