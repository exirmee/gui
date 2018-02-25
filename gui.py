import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
win=tk.Tk()
win.title("morteza app")

# Button Click Event Callback Function       
def clickMe():
    action.configure(text="hello "+name.get())

#  adding a Label

ttk.Label(win,text="enter a name:").grid(column=0, row=0)

#  adding a text
name=tk.StringVar()
nameEntered=ttk.Entry(win,width=12,textvariable=name)
nameEntered.grid(column=0,row=1)
nameEntered.focus()

#---------#
ttk.Label(win,text="choose a number :").grid(column=1,row=0)
number=tk.StringVar
numberchosen=ttk.Combobox(win,width=12,textvariable=number)
numberchosen['values']=(1,2,5,41,151)
numberchosen.grid(column=1,row=1)
numberchosen.current(0)

# Adding a Button
action = ttk.Button(win, text="Click Me!", command=clickMe)
action.grid(column=2, row=1)
#action.configure(state='disable')


#adding 3 checkbutt#
chVarDis=tk.IntVar()
check1=tk.Checkbutton(win,text="disabeld",variable=chVarDis,state='disabled')
check1.select()
check1.grid(column=0,row=2,sticky=tk.W)

chVarUn=tk.IntVar()
check2=tk.Checkbutton(win,text="unChecked",variable=chVarUn)
check2.deselect()
check2.grid(column=1,row=2,sticky=tk.W)

chVarEn=tk.IntVar()
check3=tk.Checkbutton(win,text="Checked",variable=chVarEn)
check3.select()
check3.grid(column=2,row=2,sticky=tk.W)



#scrolledtext
scrolW=30
scrolH=10
scr = scrolledtext.ScrolledText(win, width=scrolW, height=scrolH,wrap=tk.WORD)
scr.grid(column=0,columnspan=3,row=3)

#radioButt colors
color1="blue"
color2="red"
color3="gold"

#radiobutt callback
def radCall():
    radSel=radVar.get()
    if radSel==1:win.configure(background=color1)
    elif radSel==2:win.configure(background=color2)
    elif radSel==3:win.configure(background=color3)

#create 3 radiobutt
radVar=tk.IntVar()
rad1=tk.Radiobutton(win,text="color1",variable=radVar,value=1,command=radCall)
rad1.grid(column=0,row=4,sticky=tk.W)
rad2=tk.Radiobutton(win,text="color2",variable=radVar,value=2,command=radCall)
rad2.grid(column=1,row=4,sticky=tk.W)
rad3=tk.Radiobutton(win,text="color3",variable=radVar,value=3,command=radCall)
rad3.grid(column=2,row=4,sticky=tk.W)

#add 3 label  into a frame

labelsFrame=ttk.Labelframe(win,text="همه ليبل ها اينجان")
labelsFrame.grid(column=1,row=7,padx=20,pady=40)
ttk.Label(labelsFrame,text="برچسب 1").grid(column=0,row=0)
ttk.Label(labelsFrame,text="برچسب 2").grid(column=1,row=0)
ttk.Label(labelsFrame,text="برچسب 3").grid(column=2,row=0)




win.mainloop()
