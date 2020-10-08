from tkinter import *
import dic


def trans():
    z = dic.trans(word_text.get())
    list1.insert(END, z)


w = Tk()


w.wm_title('DIC')

l1 = Label(w, text='Enter Word')
l1.grid(row=0, column=0)


word_text = StringVar()
e1 = Entry(w, text=word_text)
e1.grid(row=0, column=1)


list1 = Listbox(w, height=8, width=80)
list1.grid(row=2, column=0, rowspan=4, columnspan=8)


b1 = Button(w, text='Search', width=12, command=trans)
b1.grid(row=0, column=2)


w.mainloop()
