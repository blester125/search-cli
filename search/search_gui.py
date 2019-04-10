try:
    from tkinter import *
except ImportError:
    from Tkinter import *

from search.search import get_highlighted, search, get_engine

def search_gui():
    text = " ".join(get_highlighted())
    engine = get_engine('google')

    master = Tk()
    master.wm_attributes('-type', 'splash')

    v = StringVar()
    e = Entry(master, textvariable=v, width=len(text) + 100)
    v.set(text)
    e.pack()
    e.icursor(len(text))

    def callback(event):
        query = v.get().split()
        search(engine, query)
        close(event)

    def close(event):
        exit()

    e.bind("<Return>", callback)
    e.bind("<Escape>", close)

    e.focus_force()
    mainloop()


if __name__ == "__main__":
    search_gui()