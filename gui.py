'''
file: gui.py
version: python3
author: Evan Putnam
description: A gui for AES encryption/decryption with a master password
'''
from tkinter import *
from tkinter.filedialog import askopenfilename
import hashlib
import password
import os
import tkinter.scrolledtext


class Window(Frame):

    def __init__(self, master=None):
        '''
        Initialization that calls the create windows init function
        :param master:
        '''
        Frame.__init__(self, master)
        self.master = master
        self.createWindows()

    def createWindows(self):
        '''
        Creates gui objects for view
        :return:
        '''
        #Title
        self.master.title("Encrypt/Decrypt Gui")
        self.pack(fill=BOTH, expand=1)

        #Ecnrypt button and positioning
        self.encryptButton = Button(self, text="Encrypt", command=self.encrypt)
        self.encryptButton.place(x=0, y=0)

        #Decrypt button and positioning
        self.decryptButton = Button(self, text="Decrypt", command=self.decrypt)
        self.decryptButton.place(x=75, y=0)

        #Text field for master entry
        self.masterEntry = Entry(self, text="Master Password")
        self.masterEntry.place(x=0, y=50)

        #Label descriping master entry
        self.masterLabel = Label(self, text="Master Password:")
        self.masterLabel.place(x=0,y=25)

        #Text box
        self.textBox = tkinter.scrolledtext.ScrolledText(self, height = 14, width=50, undo=FALSE)
        self.textBox.place(x=0,y=80)


    def encrypt(self):
        '''
        Function to ecrypt the data with the string in the master password
        field
        :return:
        '''
        if(self.masterEntry.get() == ""):
            self.textBox.delete('1.0', END)
            self.textBox.insert(END, "Can not have empty master password")
            return
        masterPass = hashlib.sha256(self.masterEntry.get().encode('utf-8')).digest()
        name = askopenfilename(initialdir=os.getcwd(),
                               filetypes=(("Text File", "*.txt"),("All Files", "*.*")),
                               title="Choose a file."
                               )
        password.encryptFile(name, masterPass)
        self.textBox.delete('1.0', END)
        self.textBox.insert(END, "File Encrypted, DO NOT RE-ENCRYPT")


    def decrypt(self):
        '''
        Decrypting the text file with the password from the
        master password entry field
        :return:
        '''
        if(self.masterEntry.get() == ""):
            self.textBox.delete('1.0', END)
            self.textBox.insert(END, "Can not have empty master password")
            return
        masterPass = hashlib.sha256(self.masterEntry.get().encode('utf-8')).digest()
        name = askopenfilename(initialdir=os.getcwd(),
                               filetypes=(("Text File", "*.txt"), ("All Files", "*.*")),
                               title="Choose a file."
                               )
        self.textBox.delete('1.0', END)
        try:
            self.textBox.insert(END, password.decryptFile(name, masterPass))
        except:
            self.textBox.insert(END, "Error Decrypting file.")




def main():
    '''
    Main function that creates and build the user interface
    :return:
    '''
    root = Tk()
    root.geometry("400x300")
    app = Window(root)
    root.mainloop()


if __name__ == '__main__':
    main()