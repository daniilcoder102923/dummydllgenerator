import os
import platform
import tkinter as tk
from tkinter import filedialog

def create_dll():
    number_of_dlls = int(number_entry.get())
    name_of_dlls = name_entry.get()
    selected_folder = filedialog.askdirectory()

    if platform.system() == 'Windows':
        dll_extension = '.dll'
    elif platform.system() == 'Linux' or platform.system() == 'Darwin':
        dll_extension = '.so'
    else:
        print('Unsupported operating system')
        exit()

    if name_of_dlls == '':
        name_of_dlls = 'DLL'

    for i in range(number_of_dlls):
        dll_name = f'{name_of_dlls}_{i+1}{dll_extension}'
        dll_full_path = os.path.join(selected_folder, dll_name)
        if os.path.isfile(dll_full_path):
            print(f'File {dll_name} already exists.')
            return
        else:
            open(dll_full_path, 'w').close()
            print(f'Created file {dll_name}')

root = tk.Tk()
root.title("Daniil's DLL Generator")
root.geometry('400x200')

tk.Label(root, text='Enter the number of dlls to create:').pack()
number_entry = tk.Entry(root)
number_entry.pack()

tk.Label(root, text='Enter the name of the dlls:').pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Button(root, text='Create dll files', command=create_dll).pack()

root.mainloop()