def aar():
  global count
  count+=1
  lab['font'] = ('Arial',count)
   


def aar2():
  global count
  count-=1
  if count==0:
    count=1
  lab['font']=('Arial',count)
count=1


def gr():
  lab['bg']="green"
  

def bl():
 lab['bg']="blue"
 
def rd():
 lab['bg']="red"
 
def ar():
  lab['font']=('Arial',14)

def nr():
  lab['font']=('Verdana',12)

def cl():
   lab['font']=('Calibri',10)


def wh():
  lab["fg"]="white"


def black():
  lab["fg"]="black"


def purpl():
  lab["fg"]="purple"
  


a=tk.Tk()
a.config(bg='#FFEBCD')
logo=tk.PhotoImage(file="-icon-png-image_3232032.png")
a.iconphoto(False,logo)
a.geometry("600x490+100+100")
a.title("Программа")
a.resizable(True,False)
lab=tk.Label(a,text='Привет',font=('Arial',count))
lab.grid(row=0,column=2)
arr=tk.Button(a,text='Увеличить',command=aar)
arr2=tk.Button(a,text='Уменьшить ',command=aar2)
  
green=tk.Button(a,text='зеленый',bg='green',command=gr)
blue=tk.Button(a,text='синий',bg='blue',command=bl)
red=tk.Button(a,text='красный',bg='red',command=rd)
  
arial=tk.Button(a,text='Arial',font=('Arial',14),command=ar)
tnr=tk.Button(a,text='Verdana',font=('Verdana',12),command=nr)
cl=tk.Button(a,text='Calibri',font=('Calibri',10),command=cl)

white=tk.Button(a,text="цвет текса белый",fg="white",bg="black",command=wh)
black=tk.Button(a,text="цвет текста черный",fg="black",bg="white",command=black)
purple=tk.Button(a,text="цвет текста фиолетовый",fg="purple",bg="white",command=purpl)
white.grid(row=1,column=0)
black.grid(row=1,column=1)
purple.grid(row=1,column=2)
arr.grid(row=2,column=0)
arr2.grid(row=2,column=1)
green.grid(row=3,column=0)
blue.grid(row=3,column=1)
red.grid(row=3,column=2)
arial.grid(row=4,column=0)
tnr.grid(row=4,column=1)
cl.grid(row=4,column=2)
a.mainloop()
