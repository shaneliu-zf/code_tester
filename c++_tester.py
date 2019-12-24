# -*- coding: UTF-8 -*-

def go():
    f = open('tester.cpp', 'w')
    f.write(left_text.get('1.0', 'end'))
    print('writing tester.cpp')
    f.close()
    f = open('tester.in', 'w')
    print('writing tester.in')
    f.write(input.get('1.0', 'end'))
    f.close()
    os.system("g++ tester.cpp -o tester.out")
    os.system("./tester.out < tester.in > tester.ot")
    f = open('tester.ot', 'r')
    print('reading tester.ot')
    output.delete(1.0, "end")
    output.insert(1.0,f.read())
    f.close()
    print('removing file')
    os.remove("tester.cpp")
    os.remove("tester.out")
    os.remove("tester.in")
    os.remove("tester.ot")


import tkinter as tk
import os

window = tk.Tk()
window.geometry('1000x600')
window.configure(background='white')
window.title("C++ Tester")

left_frame = tk.Frame(window)
left_frame.pack(side=tk.LEFT)

right_frame = tk.Frame(window)
right_frame.pack(side=tk.LEFT,padx=30)

left_lebel = tk.Label(left_frame, text='code:')
left_lebel.pack()

left_text = tk.Text(left_frame,width=70,height=40,relief='sunken',bg='aliceblue')
left_text.pack(padx=30,pady=10)

input_frame = tk.Frame(right_frame)
input_frame.pack()
in_lebel = tk.Label(input_frame, text=' input:',width=8)
in_lebel.pack(side=tk.LEFT)
input = tk.Text(input_frame,width=50,height=18,relief='sunken',bg='aliceblue')
input.pack(side=tk.LEFT)


bottom_button = tk.Button(right_frame, text='GO!',font=("Concole",20),command=go,width=10)
bottom_button.pack(pady=20)


output_frame = tk.Frame(right_frame)
output_frame.pack(pady=5)
out_lebel = tk.Label(output_frame, text='output:',width=8)
out_lebel.pack(side=tk.LEFT)
output = tk.Text(output_frame,width=50,height=18,relief='sunken',bg='aliceblue')
output.pack(side=tk.LEFT)

window.mainloop()
