# -*- coding: UTF-8 -*-

import tkinter as tk
import tkinter.ttk as tt
import tkinter.messagebox
import os

def cpp17():
    f=open('a.cpp', 'w')
    f.write(left_text.get('1.0', 'end'))
    f.close()
    f=open('in.txt', 'w')
    f.write(input.get('1.0', 'end'))
    f.close()
    os.system("g++ -std=c++17 a.cpp -o a.out")
    if os.path.isfile("a.out"):
        os.system("./a.out < in.txt > out.txt")
        f=open('out.txt', 'r')
        s=f.read()
        f.close()
        if s=="":
            tk.messagebox.showinfo(message="無輸出")
        output.insert(1.0,s)
        os.remove("a.out")
        os.remove("in.txt")
        os.remove("out.txt")
    else :
        tk.messagebox.showinfo(message="編譯錯誤")

def cpp():
    f=open('a.cpp', 'w')
    f.write(left_text.get('1.0', 'end'))
    f.close()
    f=open('in.txt', 'w')
    f.write(input.get('1.0', 'end'))
    f.close()
    os.system("g++ a.cpp -o a.out")
    if os.path.isfile("a.out"):
        os.system("./a.out < in.txt > out.txt")
        f=open('out.txt', 'r')
        s=f.read()
        f.close()
        if s=="":
            tk.messagebox.showinfo(message="無輸出")
        output.insert(1.0,s)
        os.remove("a.out")
        os.remove("in.txt")
        os.remove("out.txt")
    else :
        tk.messagebox.showinfo(message="編譯錯誤")

def py2():
    f=open('a.py', 'w')
    f.write(left_text.get('1.0', 'end'))
    f.close()
    f=open('in.txt', 'w')
    f.write(input.get('1.0', 'end'))
    f.close()
    os.system("python2 a.py < in.txt > out.txt")
    f = open('out.txt', 'r')
    s=f.read()
    f.close()
    if s=="":
        tk.messagebox.showinfo(message="無輸出(可能是編譯錯誤)")
    output.insert(1.0,s)
    os.remove("in.txt")
    os.remove("out.txt")

def py3():
    f=open('a.py', 'w')
    f.write(left_text.get('1.0', 'end'))
    f.close()
    f=open('in.txt', 'w')
    f.write(input.get('1.0', 'end'))
    f.close()
    os.system("python3 a.py < in.txt > out.txt")
    f = open('out.txt', 'r')
    s=f.read()
    f.close()
    if s=="":
        tk.messagebox.showinfo(message="無輸出(可能是編譯錯誤)")
    output.insert(1.0,s)
    os.remove("in.txt")
    os.remove("out.txt")

def go():
    output.delete(1.0, "end")
    if(left_combo.get()=="C++17"):
        cpp17()
    elif(left_combo.get()=="C++"):
        cpp()
    elif(left_combo.get()=="Python3"):
        py3()
    elif(left_combo.get()=="Python2"):
        py2()
    else :
        tk.messagebox.showinfo(message="尚未有該程式語言")

window = tk.Tk()
window.geometry('1000x600')
window.configure(background='white')
window.title("Code Tester")

left_frame = tk.Frame(window)
left_frame.pack(side=tk.LEFT)

left_lebel = tk.Label(left_frame, text='code:')
left_lebel.pack()

left_combo = tt.Combobox(left_frame,width=50,value=['C++17','C++','Python2','Python3'])
left_combo.current(0)
left_combo.pack()

left_text = tk.Text(left_frame,width=70,height=40,bg='aliceblue')
left_text.pack(padx=30,pady=10)

right_frame = tk.Frame(window)
right_frame.pack(side=tk.LEFT,padx=30)

input_frame = tk.Frame(right_frame)
input_frame.pack()

in_lebel = tk.Label(input_frame, text=' input:',width=8)
in_lebel.pack(side=tk.LEFT)

input = tk.Text(input_frame,width=50,height=18,bg='aliceblue')
input.pack(side=tk.LEFT)

bottom_button = tk.Button(right_frame, text='GO!',font=("Concole",20),command=go,width=10)
bottom_button.pack(pady=20)

output_frame = tk.Frame(right_frame)
output_frame.pack(pady=5)

out_lebel = tk.Label(output_frame, text='output:',width=8)
out_lebel.pack(side=tk.LEFT)

output = tk.Text(output_frame,width=50,height=18,bg='aliceblue')
output.pack(side=tk.LEFT)

window.mainloop()
