import json
from os import getcwd
from PIL import Image, ImageTk
from tkinter import *
from tkinter import ttk, filedialog

# The logic:
def save():
    doc = 'data.json' # This is the data file, we will change.
    src = open_data(doc)
    vals = get_gui_values()
    src = write_data(src,vals)
    save_changes(src, doc)
    print(open(doc,'r').read)
	
def open_data(filename): # Here we open the given filename file, and make it an object.
    with open(filename,'r') as data:
        data = json.loads(data.read())
    return data

def get_gui_values(): # Here we get all the inputs from the gui, and set them as a list.
    article = str(_art_name.get())
    title = str(_art_title.get())
    text = str(_art_text_entry.get('1.0',END))
    return [article, title, text]

def write_data(arg, values): # Here we get the data object('arg'), and append to it the new values.
    #print(article, title, text)
    arg[values[0]] = {}
    arg[values[0]]['name'] = values[1]
    arg[values[0]]['text'] = values[2]
    return arg

def save_changes(source, document): # Here we get the data object('source'), and write it to the data file('document').
    with open(document, 'w') as document:
        document.write(json.dumps(source))
####################################################


		
def choose_image():
    image = get_img_dir()
    image = create_img_object(image)
    set_img(image)
	
def get_img_dir():
    pathname = getcwd()+'/images'
    filename = filedialog.askopenfilename(initialdir=pathname, title='Select image file:', filetypes=(('JPEG files', ('*.jpg','*.jpeg')),('PNG files', '*.png')))
    print(filename)
    return filename
	
def create_img_object(arg):
    photo = Image.open(arg)
    photo.thumbnail(120,200,Image.ANTIALIAS)
    return photo
	
def set_img(arg):
    pass
    
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
#############################################################
	
# Define the article text frame:
    _art_text_frame = ttk.LabelFrame(_mainframe, padding='5 5 5 5', text='Article:')
    _art_text_frame.grid(row=1,column=0, sticky=(E, W, S, N))
    _art_text_frame.columnconfigure(0, weight=1)
    _art_text_frame.columnconfigure(1, weight=1)
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
    _art_text_entry.grid(row=1, column=0, sticky=(W, E, S, N), padx=5)
	
# Define the image choose button:
    _img_btn = ttk.Button(_art_text_frame, text='Choose image', command=choose_image)
    _img_btn.grid(row=0, column=1, sticky=E, padx=5)
	
# Define the image canvas:
    _img_canvas = Canvas(_art_text_frame, width=120, height=200, bg='red')
    _img_canvas.grid(row=1, column=1, sticky=(E, W, S, N), padx=5)
	
    _root.mainloop()