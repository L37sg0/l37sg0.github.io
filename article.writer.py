import json
from tkinter import *
from tkinter import ttk

# the logic:
def save():
    source = open_data()
    write_data()
    print(source)
	
def open_data():
    with open('data.json','r') as data:
        data = json.loads(data.read())
    return data

def write_data():
    article = str(_art_name.get())
    title = str(_art_title.get())
    text = str(_art_text_entry.get())
    print(article, title, text)

# the gui:
if __name__ == '__main__':
# Define the root window:    
    _root = Tk()
    _root.title('Article Writer')
    _root.columnconfigure(0, weight=1)
    _root.rowconfigure(0, weight=1)
    _root.geometry('720x480')

# Define the mainframe:
    _mainframe = ttk.Frame(_root, padding='5 5 5 5')
    _mainframe.grid(row=0, column=0, sticky=(E, W, S, N))
    _mainframe.columnconfigure(0, weight=1)
    #_mainframe.rowconfigure(0, weight=1)
    _mainframe.rowconfigure(1, weight=1)
	
# Define article name frame:
    _art_name_frame = ttk.LabelFrame(_mainframe, padding='5 5 5 5', text='Enter Article Name:')
    _art_name_frame.grid(row=0, column=0, sticky=(E, W, S, N))
    _art_name_frame.columnconfigure(0, weight=1)

# Define the article name entry:
    _art_name = StringVar()
    _art_name.set('New Article')
    _name_entry = ttk.Entry(_art_name_frame, width=40, textvariable=_art_name)
    _name_entry.grid(row=0, column=0, sticky=(E, W), padx=5)
    _name_entry.columnconfigure(0, weight=1)
# Define the Save- button:
    _save_btn = ttk.Button(_art_name_frame, text='Save Article', command=save)
    _save_btn.grid(row=0, column=1, sticky=E, padx=5)
	
# Define the article text frame:
    _art_text_frame = ttk.LabelFrame(_mainframe, padding='5 5 5 5', text='Article:')
    _art_text_frame.grid(row=1,column=0, sticky=(E, W, S, N))
    _art_text_frame.columnconfigure(0, weight=1)
    #_art_text_frame.rowconfigure(0, weight=1)
    _art_text_frame.rowconfigure(1, weight=1)
	
# Define the article title:
    _art_title = StringVar()
    _art_title.set('Title')
    _art_title_entry = ttk.Entry(_art_text_frame, width=40, textvariable=_art_title)
    _art_title_entry.grid(row=0, column=0, sticky=(W, E), padx=5)
# Define the article text:
    _art_text = StringVar()
    _art_text.set('Text Here...')
    _art_text_entry = Text(_art_text_frame,width=40, height=20, bg='white', fg='black')
    _art_text_entry.grid(row=1, column=0, sticky=(W, E), padx=5)
	
	
    _root.mainloop()