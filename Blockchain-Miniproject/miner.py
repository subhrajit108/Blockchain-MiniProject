from tkinter import ttk
from tkinter import *
from hashlib import sha256
import pyscrypt
import os



class Miner:
    blocknumber = 0

    def __init__(self, window, master, last_hash):
        if (os.path.exists("vehicle_information.txt")):
            f = open("vehicle_information.txt", "r")
            transactions = f.read().split('\n')
            transactions.pop()
            f.close()
            window.title("Transactions")
            l = Label(window, text="Verify Transaction")
            T = Text(window, height=5, width=52)

            total = len(transactions)
            self.count = 0
            self.new_hash = ""
            transaction = str(transactions[self.count]).replace(',', '\n')
            T.insert(END, transaction)
            T.configure(state='disabled')
            b1 = Button(window, text="Verify and Add to Block",
                        command=lambda: self.add(transactions, window, master, last_hash))
            b2 = Button(window, text="Next Transaction",
                        command=lambda: self.next(transactions, T, total, window, master))
            b3 = Button(window, text="Exit", command=lambda: self.exit(master, window, 0))
            l.pack()
            T.pack()
            b1.pack()
            b2.pack()
            b3.pack()
        else:
            window.title("Transactions")
            window.geometry('400x100')
            l = Label(window, text="No transaction present in transaction repository")
            b = Button(window, text="Exit", command=lambda: self.exit(master, window, 0))
            l.pack()
            b.pack()

    def add(self, transactions, window, master, last_hash):
        window.withdraw()
        mine_window = Toplevel(window)
        mine_window.title("Mining...")
        mine_window.geometry('400x150')
        l = Label(mine_window, text="Transaction added to block")
        self.T = Text(mine_window, height=5, width=52)
        transaction = str(transactions[self.count]).replace(',', '\n')
        self.T.insert(END, transaction)
        self.T.configure(state='disabled')
        self.b = Button(mine_window, text="Start Mining the blocks",
                        command=lambda: self.mine(transactions, transaction, last_hash, mine_window, window, master))
        l.pack()
        self.T.pack()
        self.b.pack()

    def next(self, transactions, T, total, window, master):
        self.count += 1
        if (self.count == total):
            window.withdraw()
            end_window = Toplevel(window)
            end_window.title("Transactions in Blockchain system")
            end_window.geometry('400x120')
            l = Label(end_window, text="End of transactions")
            b = Button(end_window, text="Go back to Login page", command=lambda: self.exit(master, window, end_window))
            l.pack()
            b.pack()
        else:
            T.configure(state="normal")
            T.delete('1.0', 'end')
            transaction = str(transactions[self.count]).replace(',', '\n')
            T.insert(END, transaction)
            T.configure(state='disabled')

    def exit(self, root, master, window):
        master.destroy()
        if (window != 0):
            window.destroy()
        root.deiconify()

    def SCRYPT(self, text):
        salt = os.urandom(8) #initially 8
        b = bytes(text, 'utf-8')
        digest = pyscrypt.hash(b, salt, 8, 2, 1, 32)
        return str(digest.hex())

    def mine(self, transactions, transaction, last_hash, window, master, root):
        if (self.b['text'] == "EXIT"):
            self.exit(root, master, window)
        else:
            difficulty = 2 #initially 2
            prefix_str = '0' * difficulty
            self.b["state"] = 'disabled'
            self.T.configure(state='normal')
            self.T.delete('1.0', 'end')
            self.T.insert(INSERT, "Mining in process...")
            self.T.configure(state='disabled')
            self.T.update_idletasks()
            self.b.update_idletasks()
            Miner.blocknumber += 1
            for nonce in range(10000000000):
                mine_string = transaction + str(last_hash) + str(Miner.blocknumber)
                text = mine_string + str(nonce)
                new_h = self.SCRYPT(text)
                if new_h.startswith(prefix_str):
                    print("Successfully mined with nonce:", nonce)
                    self.new_hash = new_h
                    file = open("blocks.txt", "a+")
                    file.write("Block number: " + str(Miner.blocknumber) + ", ")
                    file.write("Transaction: {" + transaction.replace('\n', ',') + "}, ")
                    file.write("Nonce: " + str(nonce) + ", ")
                    file.write("Hash: " + str(new_h) + "\n")
                    file.close()
                    transactions.pop(self.count)
                    string = '\n'.join(transactions)
                    file = open("vehicle_information.txt", "w+")
                    file.write(string + "\n")
                    file.close()
                    last_hash = str(new_h)
                    self.T.configure(state='normal')
                    self.T.insert(INSERT, "\nNONCE: " + str(nonce))
                    self.T.insert(END, "\nNEW HASH: " + str(new_h))
                    self.T.configure(state='disabled')
                    self.b["state"] = 'normal'
                    self.b['text'] = "EXIT"
                    return
            # raise BaseException("Max limit exceeded")
            self.T.configure(state='normal')
            self.T.insert(END, "\nMax limit exceeded")
            self.T.configure(state='disabled')
            self.b["state"] = 'normal'
            self.b['text'] = "EXIT"
            Miner.blocknumber -= 1