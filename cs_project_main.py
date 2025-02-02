import tkinter as tk
import subprocess as sp

rt_win = None
connect = None


# Open Reaction Test
def open_rt():
    sp.run(['python', 'reaction_test.py'])

# Open Connect_4 Game
def open_connect():
    sp.run(['python', 'connect4_graphics.py'])


# Main Window
root = tk.Tk()
root.title("CS Project")
root.geometry("250x100")


btn_rt = tk.Button(root, text="Reaction Test", command=open_rt)
btn_rt.pack(pady=10)


btn_connect = tk.Button(root, text="Connect 4", command=open_connect)
btn_connect.pack(pady=10)

root.mainloop()
