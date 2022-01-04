from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
compiler = Tk()
compiler.title('AJ IDE')
file_path = ''


def set_filepath(path):
    global file_path
    file_path = path

def open_file():
    path = askopenfilename(filetypes=[('Python Files', '*.py')])
    with open(path, 'r') as file:
        program = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', program)
        set_filepath(path)

def save_as():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    else:
        path = file_path
    with open(path, 'w') as file:
        program =editor.get('1.0', END)
        file.write(program)
        set_filepath(path)


def run():
    command = f'python {file_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output,error = process.communicate()
    program_output.insert('1.0',output)
menubar = Menu(compiler)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='Open', command=open_file)
filemenu.add_command(label='Save', command=save_as)
filemenu.add_command(label='Save As', command=save_as)
filemenu.add_command(label='Exit', command=exit)
menubar.add_cascade(label='File', menu=filemenu)

runbar = Menu(menubar, tearoff=0)
runbar.add_command(label='Run', command=run)
menubar.add_cascade(label='Run Module', menu=runbar)
compiler.config(menu=menubar)

Shell = Menu(menubar, tearoff=0)
Shell.add_command(label='Shell', command=run)
menubar.add_cascade(label='Shell', menu=Shell)
compiler.config(menu=menubar)

Debug = Menu(menubar, tearoff=0)
Debug.add_command(label='Debug', command=run)
menubar.add_cascade(label='Debug', menu=Debug)
compiler.config(menu=menubar)

Option = Menu(menubar, tearoff=0)
Option.add_command(label='Option', command=run)
menubar.add_cascade(label='Option', menu=Option)
compiler.config(menu=menubar)

Windows = Menu(menubar, tearoff=0)
Windows.add_command(label='Windows', command=run)
menubar.add_cascade(label='Windows', menu=Windows)
compiler.config(menu=menubar)

Help = Menu(menubar, tearoff=0)
Help.add_command(label='Help', command=run)
menubar.add_cascade(label='Help', menu=Help)
compiler.config(menu=menubar)

editor = Text()
editor.pack()

program_output = Text(height=10)
program_output.pack()

compiler.mainloop()