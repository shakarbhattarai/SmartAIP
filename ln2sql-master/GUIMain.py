from Tkinter import *
from DatabaseConnection import get_desc

root = tk()
root.title('Mantis Automation: AUTO SQL GENERATOR')
tk.Label(text='Enter MANTIS NUMBER').pack(side=tk.TOP, padx=100, pady=30)

entry = tk.Entry(root, width=100)
entry.pack(side=TOP,padx=10,pady=10)

tk.Label(text='Description Goes Here').pack(side=tk.BOTTOM, padx=100, pady=30)
entry2 = tk.Entry(root, width=100)
entry2.pack(side=tk.BOTTOM, padx=30, pady=30)

def onok():
    print get_desc('12345')

tk.Button(root, width=50, text='OK', command=onok).pack(side=tk.BOTTOM, padx=20, pady=90)

root.mainloop()