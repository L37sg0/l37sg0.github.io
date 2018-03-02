import json
import shutil
import ntpath
from os import getcwd, listdir
import PIL.Image
import PIL.ImageTk
from tkinter import *
from tkinter import ttk, filedialog

class app:
    def __init__(self,window):
    # Define the mainframe:
        self._mainframe = ttk.Frame(window, padding='5 5 5 5')
        self._mainframe.grid(row=0, column=0, sticky=(E, W, S, N))
        self._mainframe.columnconfigure(0, weight=1)
        #self._mainframe.rowconfigure(0, weight=1)
        self._mainframe.rowconfigure(1, weight=1)

    # Define article name frame:
        self._art_name_frame = ttk.LabelFrame(self._mainframe, padding='5 5 5 5', text='Enter Article Name:')
        self._art_name_frame.grid(row=0, column=0, sticky=(E, W, S, N))
        self._art_name_frame.columnconfigure(0, weight=1)
        
    # Define the article name entry:
        self._art_name = StringVar()
        self._art_name.set('New Article')
        self._name_entry = ttk.Entry(self._art_name_frame, width=40, textvariable=self._art_name)
        self._name_entry.grid(row=0, column=0, sticky=(E, W), padx=5)
        self._name_entry.columnconfigure(0, weight=1)

    # Define the Save- button:
        self._save_btn = ttk.Button(self._art_name_frame, text='Save Article', command=self.save)
        self._save_btn.grid(row=0, column=1, sticky=E, padx=5)
#############################################################
	
    # Define the article text frame:
        self._art_text_frame = ttk.LabelFrame(self._mainframe, padding='5 5 5 5', text='Article:')
        self._art_text_frame.grid(row=1,column=0, sticky=(E, W, S, N))
        self._art_text_frame.columnconfigure(0, weight=1)
        self._art_text_frame.columnconfigure(1, weight=1)
        self._art_text_frame.rowconfigure(1, weight=1)

    # Define the article title:
        self._art_title = StringVar()
        self._art_title.set('Title')
        self._art_title_entry = ttk.Entry(self._art_text_frame, width=40, textvariable=self._art_title)
        self._art_title_entry.grid(row=0, column=0, sticky=(W, E), padx=5)

    # Define the article text:
        self._art_text = StringVar()
        self._art_text.set('Text Here...')
        self._art_text_entry = Text(self._art_text_frame,width=40, height=20, bg='white', fg='black')
        self._art_text_entry.grid(row=1, column=0, sticky=(W, E, S, N), padx=5)
		
    # Define the image choose button:
        self._img_btn = ttk.Button(self._art_text_frame, text='Choose image', command=self.choose_image)
        self._img_btn.grid(row=0, column=1, sticky=E, padx=5)

    # Define the image frame:
        self._img_name = StringVar()
        self._img_name.set(None)
        self._img_frame = ttk.LabelFrame(self._art_text_frame, padding='5 5 5 5', text='Image:')
        self._img_frame.grid(row=1, column=1, sticky=(E, W, S, N))
        self._img_frame.columnconfigure(0, weight=1)
        self._img_frame.rowconfigure(0, weight=1)

    # Define the image canvas:
        self._img_label = ttk.Label(self._img_frame, text='image here', image=None)
        self._img_label.grid(row=0, column=0, padx=5, sticky=(E, W, S, N))

    # The logic:
    def save(self):
        self.doc = 'data.json' # This is the data file, we will change.
        self.src = self.open_data(self.doc)
        self.vals = self.get_gui_values()
        self.src = self.write_data(self.src, self.vals)
        self.save_changes(self.src, self.doc)
        print(open(self.doc,'r').read)
	
    def open_data(self, filename): # Here we open the given filename file, and make it an object.
        self.filename = filename
        with open(self.filename,'r') as data:
            data = json.loads(data.read())
        return data

    def get_gui_values(self): # Here we get all the inputs from the gui, and set them as a list.
        self.article = str(self._art_name.get())
        self.title = str(self._art_title.get())
        self.text = str(self._art_text_entry.get('1.0',END))
        self.image = self._img_name.get()
        return [self.article, self.title, self.text, self.image]

    def write_data(self, arg, values): # Here we get the data object('arg'), and append to it the new values.
        #print(article, title, text)
        self.arg = arg
        self.values = values
        self.arg[self.values[0]] = {}
        self.arg[self.values[0]]['name'] = self.values[1]
        self.arg[self.values[0]]['text'] = self.values[2]
        self.arg[self.values[0]]['image'] = self.values[3]
        return arg

    def save_changes(self, source, document): # Here we get the data object('source'), and write it to the data file('document').
        self.source = source
        self.document = document
        with open(self.document, 'w') as document:
            document.write(json.dumps(self.source))
####################################################
		
    def choose_image(self):
        self.dir = self.get_img_dir()		# Get the choosen image location 
        self.image = self.path_leaf(self.dir)
        # self.image = self.check_img_location(self.image) # Check if image is in 'images' folder, if it's not copyes it to 'images'
        self.image = self.create_img_object(self.image)
        self.set_img(self.image)
	
    def get_img_dir(self):
        self.pathname = getcwd()+'/images'
        self.filename = (filedialog.askopenfilename(initialdir=self.pathname, title='Select image file:', filetypes=(('JPEG files', ('*.jpg','*.jpeg')),('PNG files', '*.png'))))
        print(self.filename)
        return self.filename
		
    def path_leaf(self, path):
        self.path = path
        self.head, self.tail = ntpath.split(self.path)
        return self.tail or ntpath.basename(self.head)
###########

    def check_img_location(self, file, or_dir ):
        self.file = file
        self.or_dir = or_dir
        self.local_dir = getcwd()+'/images'
        if file not in listdir(self.local_dir):
            shutil.copy(src=self.or_dir, dst=self.local_dir) 
        
                				
##############
    def create_img_object(self, arg):
        self.arg = arg
        self.photo = PIL.Image.open(self.arg)
        self.photo = self.photo.resize((120,200),PIL.Image.ANTIALIAS)
        self.photo = PIL.ImageTk.PhotoImage(self.photo)
        return self.photo
	
    def set_img(self, arg):
        self.arg = arg
        self._img_label.configure(image=self.arg)
        self._img_name.set(self.arg)


def main():    
    _root = Tk()
    _root.title('Article Writer')
    _root.columnconfigure(0, weight=1)
    _root.rowconfigure(0, weight=1)
    _root.geometry('505x360')
    app(_root)
    _root.mainloop()

if __name__ == '__main__':
    main() 
