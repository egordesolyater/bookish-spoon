a=tk.Tk()
a.config(bg='#FFEBCD')
logo=tk.PhotoImage(file="-icon-png-image_3232032.png")
a.iconphoto(False,logo)
a.geometry("625x335+100+100")
a.title("Программа")
a.resizable(True,False)
g=''
def h1():
  global g
  g+=(hel1[ 'text' ])
  lab["text"]=g
  


def h2():
  global g
  g+=(hel2[ 'text' ])
  lab["text"]=g
  

def h3():
  global g
  g+=(hel3[ 'text' ])
  lab["text"]=g
  
def h4():
  global g
  g+=(hel4[ 'text' ])
  lab["text"]=g
  
def h5():
  global g
  g+=(hel5[ 'text' ])
  lab["text"]=g
  
def h6():
  global g
  g+=(hel6[ 'text' ])
  lab["text"]=g
  
def h7():
  global g
  g+=(hel7[ 'text' ])
  lab["text"]=g
  
def h8():
  global g
  g+=(hel8[ 'text' ])
  lab["text"]=g
 
def h9():
  global g
  g+=(hel9[ 'text' ])
  lab["text"]=g
  

def h0():
  global g
  g+=(hel0[ 'text' ])
  lab["text"]=g
  


def mn():
  global g
  g+=(min["text"])
  lab["text"]=g
def plu():
  global g
  g+=(pl["text"])
  lab["text"]=g
  
def um():
  global g
  g+=(umn["text"])
  lab["text"]=g
def dlen():
  global g
  g+=(dl["text"])
  lab["text"]=g
def cle():
  global g 
  g=''
  lab["text"]=g
  
def rav0():
  global g
  lab["text"]=g+'='+str(eval(g))



hel1=tk.Button(a,text="1",width=15,height=3,command=h1,font=("Arial",10))
hel2=tk.Button(a,text="2",width=15,height=3,command=h2,font=("Arial",10))
hel3=tk.Button(a,text="3",width=15,height=3,command=h3,font=("Arial",10))
hel4=tk.Button(a,text="4",width=15,height=3,command=h4,font=("Arial",10))
hel5=tk.Button(a,text="5",width=15,height=3,command=h5,font=("Arial",10))
hel6=tk.Button(a,text="6",width=15,height=3,command=h6,font=("Arial",10))
hel7=tk.Button(a,text="7",width=15,height=3,command=h7,font=("Arial",10))
hel8=tk.Button(a,text="8",width=15,height=3,command=h8,font=("Arial",10))
hel9=tk.Button(a,text="9",width=15,height=3,command=h9,font=("Arial",10))
hel0=tk.Button(a,text="0",width=15,height=3,command=h0,font=("Arial",10))
hel1.grid(row=1,column=0)
hel2.grid(row=1,column=1)
hel3.grid(row=1,column=2)
hel4.grid(row=2,column=0)
hel5.grid(row=2,column=1)
hel6.grid(row=2,column=2)
hel7.grid(row=3,column=0)
hel8.grid(row=3,column=1)
hel9.grid(row=3,column=2)
hel0.grid(row=5,column=1)
min=tk.Button(a,text="-",width=15,height=3,command=mn,font=("Arial",10),bg="red",fg="blue")
pl=tk.Button(a,text="+",width=15,height=3,command=plu,font=("Arial",10),bg="blue",fg="red")
dl=tk.Button(a,text="//",width=15,height=3,command=dlen,font=("Arial",10),bg="red",fg="blue")
umn=tk.Button(a,text="*",width=15,height=3,command=um,font=("Arial",10),bg="blue",fg="red")
rav=tk.Button(a,text="=",width=15,height=3,command=rav0,font=("Arial",10),bg="blue")
clear=tk.Button(a,text="C",width=15,height=3,command=cle,font=("Arial",10),bg="red")
min.grid(row=1,column=3)
pl.grid(row=2,column=3)
dl.grid(row=3,column=3)
umn.grid(row=5,column=3)
rav.grid(row=5,column=0)
clear.grid(row=5,column=2)
lab=tk.Label(text='',width=20,height=3,font=("Arial",15))
lab.grid(row=0,column=0,columnspan=4,stick='we')
a.mainloop()
