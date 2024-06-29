import tkinter as tk
from tkinter import messagebox
def add_digit(digit):
  value=pr.get()
  if value[0]=='0' and len(value)==1:
    value=value[1:]
  pr.delete(0,tk.END)
  pr.insert(0,value+digit)

def add_operation(operation):
  value=pr.get()
  if value[-1] in '-+/*':
    value=value[:-1]
  elif '+' in value or '-' in value or '*' in value or '/' in value:
    calculate()
    value=pr.get()
  pr.delete(0,tk.END)
  pr.insert(0,value+operation)

def calculate():
  value=pr.get()
  if value[-1] in '+-/*':
    operation = value[-1]
    value=value[:-1]+operation+value[:-1]
  pr.delete(0,tk.END)
  try:
    pr.insert(0,eval(value))
  except (NameError,SyntaxError):
    messagebox.showinfo('Внимание','Нужно вводить только цифры!! Вы ввели другие символы!')
    pr.insert(0,'0')
  except ZeroDivisionError:
    messagebox.showinfo("Внимание",'Делить на ноль нельзя!')
    pr.insert(0,'0')
    
def make_digit_button(digit):
  return tk.Button(a,text=digit ,bd=5,font=('Arial',13),command= lambda: add_digit(digit))

def make_operation_button(operation):
  return tk.Button(a,text=operation ,bd=5,font=('Arial',13),fg='red',command= lambda: add_operation(operation))

def make_calc_button(operation):
  return tk.Button(a,text=operation ,bd=5,font=('Arial',13),fg='red',command= lambda: calculate())

def clear():
  pr.delete(0,tk.END)
  pr.insert(0,"0")

def make_clear_button():
  return tk.Button(a,text='C',bd=5,font=('Arial',13),fg='red',command= lambda: clear())

def press_key(event):
  if event.char.isdigit():
    add_digit(event.char)
  elif event.char in '+-/*':
    add_operation(event.char)
  elif event.char =='\r':
    calculate()
    


a=tk.Tk()
a.config(bg='#FFEBCD')
a.geometry("240x270")
a.title("Калькулятор")
a.resizable(True,False)
a.bind('<Key>',press_key)

pr=tk.Entry(a,justify=tk.RIGHT,font=("Arial",15),width=15)
pr.insert(0,'0')
pr.grid(row=0,column=0,columnspan=4,sticky="we",padx=5)
make_digit_button('1').grid(row=1,column=0,sticky="wens",padx=5,pady=5,)
make_digit_button('2').grid(row=1,column=1,sticky="wens",padx=5,pady=5)
make_digit_button('3').grid(row=1,column=2,sticky="wens",padx=5,pady=5)
make_digit_button('4').grid(row=2,column=0,sticky="wens",padx=5,pady=5)
make_digit_button('5').grid(row=2,column=1,sticky="wens",padx=5,pady=5)
make_digit_button('6').grid(row=2,column=2,sticky="wens",padx=5,pady=5)
make_digit_button('7').grid(row=3,column=0,sticky="wens",padx=5,pady=5)
make_digit_button('8').grid(row=3,column=1,sticky="wens",padx=5,pady=5)
make_digit_button('9').grid(row=3,column=2,sticky="wens",padx=5,pady=5)
make_digit_button('0').grid(row=4,column=1,sticky="wens",padx=5,pady=5)

make_operation_button('+').grid(row=1,column=3,sticky="wens",padx=5,pady=5)
make_operation_button('-').grid(row=2,column=3,sticky="wens",padx=5,pady=5)
make_operation_button('*').grid(row=3,column=3,sticky="wens",padx=5,pady=5)
make_operation_button('/').grid(row=4,column=3,sticky="wens",padx=5,pady=5)

make_calc_button('=').grid(row=4,column=0,sticky="wens",padx=5,pady=5)

make_clear_button().grid(row=4,column=2,sticky='wens',padx=5,pady=5)

a.grid_rowconfigure(1,minsize=60)
a.grid_rowconfigure(2,minsize=60)
a.grid_rowconfigure(3,minsize=60)
a.grid_rowconfigure(4,minsize=60)
a.grid_columnconfigure(0,minsize=60)
a.grid_columnconfigure(1,minsize=60)
a.grid_columnconfigure(2,minsize=60)
a.mainloop()
