import hashlib
import os
from tkinter import *
from tkinter import ttk
from client import *
from miner import *


class Login:
    def __init__(self, master):
        master.title("Login into Traffic Centre Blockchain System")
        master.geometry('500x250')
        btn1 = ttk.Button(master, text="Login As Certificate Authority", width=20, command=lambda: self.btn(master, "Certificate Authority")).grid(
            row=0, column=0, pady=10, padx=150)
        btn2 = ttk.Button(master, text="Login As Blockchain System Miner", width=20, command=lambda: self.btn(master, "Blockchain System Miner")).grid(
            row=1, column=0, padx=150)
        btn3 = ttk.Button(master, text="View Blocks in System", width=20, command=lambda: self.btn(master, "Blocks in System")).grid(row=2,
                                                                                                                 column=0,
                                                                                                                 pady=10)
        btn4 = ttk.Button(master, text="Exit", width=20, command=lambda: self.btn(master, "Exit")).grid(row=3, column=0)

    def btn(self, master, log):
        master.withdraw()
        if (log == "Certificate Authority"):
            form_window = Toplevel(master)
            new_form = Form(form_window, master)
        elif (log == "Blockchain System Miner"):
            # show transactions appended
            miner_window = Toplevel(master)
            new_mine = Miner(miner_window, master, last_block_hash)
            # to verify and mine
        elif (log == "Blocks in System"):
            block_window = Toplevel(master)
            block_window.title("Blocks in System")
            if (os.path.exists("blocks.txt")):
                f = open("blocks.txt", "r")
                blocks = f.read().split("\n")
                f.close()
                text = "\n".join(blocks)
                l = Label(block_window, text="Blocks")
                T = Text(block_window)
                T.insert(END, text)
                T.configure(state='disabled')
                b = Button(block_window, text="Exit", command=lambda: exit(block_window, master))
                l.pack()
                T.pack()
                b.pack()
            else:
                block_window.geometry('420x200')
                l = Label(block_window, text="The blockchain does not have any blocks")
                b = Button(block_window, text="Exit", command=lambda: exit(block_window, master))
                l.pack()
                b.pack()
        else:
            if (os.path.exists("vehicle_information.txt")):
                os.remove("vehicle_information.txt")
            if (os.path.exists("blocks.txt")):
                os.remove("blocks.txt")
            master.destroy()


class Block:
    def __init__(self):
        self.verified_transactions = []
        self.previous_block_hash = ""
        self.Nonce = ""


transactions = []
last_block_hash = ""
last_transaction_index = 0


def exit(block_window, master):
    block_window.destroy()
    master.deiconify()


def main():
    root = Tk()
    app = Login(root)
    root.mainloop()


if __name__ == '__main__':
    if (os.path.exists("vehicle_information.txt")):
        os.remove("vehicle_information.txt")
    if (os.path.exists("blocks.txt")):
        os.remove("blocks.txt")
    t0 = 'Genesis Block'
    # salt=os.urandom(8)
    digest = hash(t0)
    last_block_hash = digest
    main()
