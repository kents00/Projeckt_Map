import sys
import os
import uuid
from PIL import Image, ImageTk


try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import gui_support
import random
from lib.vegetation import *
from functools import partial  # Required for passing functions as arguments


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    gui_support.set_Tk_var()
    top = Projeckt_Map (root)
    gui_support.init(root, top)
    root.mainloop()

w = None
def create_Projeckt_Map(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Projeckt_Map(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    gui_support.set_Tk_var()
    top = Projeckt_Map (w)
    gui_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Projeckt_Map():
    global w
    w.destroy()
    w = None

def get_call(PositionX, PositionY, color_range, scale, octaves, persistence, lacunarity, threshold):
        PositionX = (PositionX.get())
        PositionY = (PositionY.get())
        color_range = (color_range.get())
        scale = (scale.get())
        octaves = (octaves.get())
        persistence = (persistence.get())
        lacunarity = (lacunarity.get())
        threshold = (threshold.get())

        map_data = GenerateMap(
                (int(600), int(600)), 
                x_starting_pos=int(PositionX), 
                y_starting_pos=int(PositionY),
                color_range=int(color_range),
                scale= float(scale),
                octaves= int(octaves), 
                persistance= float(persistence),
                lacunarity= float(lacunarity),
                threshold= float(threshold))

        Generate = map_data.generate_map("Generate")
        Output = Image.fromarray((Generate).astype('uint8')).save("result_veg.jpeg")
        return Output

class Projeckt_Map:

        def __init__(self, top=None):
                #Inputed values
                Octaves = tk.IntVar()
                Persistence = tk.DoubleVar()
                Lacunarity = tk.DoubleVar()
                Scale = tk.IntVar()
                PositionX = tk.IntVar()
                PositionY = tk.IntVar()
                Color_range = tk.IntVar()
                threshold = tk.DoubleVar()

                '''This class configures and populates the toplevel window.
                top is the toplevel containing window.'''
                _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
                _fgcolor = '#000000'  # X11 color: 'black'
                _compcolor = '#d9d9d9' # X11 color: 'gray85'
                _ana1color = '#d9d9d9' # X11 color: 'gray85'
                _ana2color = '#ececec' # Closest X11 color: 'gray92'
                self.style = ttk.Style()

                if sys.platform == "win32":
                        self.style.theme_use('winnative')
                self.style.configure('.',background=_bgcolor)
                self.style.configure('.',foreground=_fgcolor)
                self.style.configure('.',font="TkDefaultFont")
                self.style.map('.',background=
                [('selected', _compcolor), ('active',_ana2color)])

                top.geometry("600x450+349+122")
                top.minsize(120, 1)
                top.maxsize(1370, 749)
                top.resizable(1,  1)
                top.title("Projeckt_Map")
                top.configure(background="#d9d9d9")
                top.configure(highlightbackground="#d9d9d9")
                top.configure(highlightcolor="black")

                self.Preview_Image = tk.Canvas(top, height=600, width=600)
                self.Preview_Image.pack()

                self.image = (Image.open("lib/bin/No_image.jpeg"))
                self.resize_image = self.image.resize((600, 450), Image.ANTIALIAS)
                self.img = ImageTk.PhotoImage(self.resize_image)

                self.update_img = ImageTk.PhotoImage(Image.open("lib/bin/result_veg.jpeg"))

                self.image_id = self.Preview_Image.create_image(-115, -50, image=self.img, anchor=tk.NW, )
                self.Preview_Image.place(relx=0.017, rely=0.067, relheight=0.784
                        , relwidth=0.605)

                self.Position_seed = tk.Message(top)
                self.Position_seed.place(relx=0.7, rely=0.111, relheight=0.029, relwidth=0.067)
                self.Position_seed.configure(background="#d9d9d9",
                                foreground="#000000", 
                                highlightbackground="#d9d9d9",
                                highlightcolor="black",
                                text='''Seed :''',
                                width=40
                                )

                self.Color_Range = tk.Message(top)
                self.Color_Range.place(relx=0.633, rely=0.2, relheight=0.029, relwidth=0.133)
                self.Color_Range.configure(background="#d9d9d9",
                                        foreground="#000000",
                                        highlightbackground="#d9d9d9",
                                        highlightcolor="black",
                                        text='''Color Range :''',
                                        width=80
                                )

                self.Scale = tk.Message(top)
                self.Scale.place(relx=0.7, rely=0.289, relheight=0.029, relwidth=0.067)
                self.Scale.configure(background="#d9d9d9",
                                foreground="#000000",
                                highlightbackground="#d9d9d9",
                                highlightcolor="black",
                                text='''Scale :''',
                                width=40
                                )

                self.Octaves = tk.Message(top)
                self.Octaves.place(relx=0.667, rely=0.378, relheight=0.029, relwidth=0.1)
                self.Octaves.configure(background="#d9d9d9",
                                foreground="#000000",
                                highlightbackground="#d9d9d9",
                                highlightcolor="black",
                                text='''Octaves :''',
                                width=60
                                )

                self.Persistance = tk.Message(top)
                self.Persistance.place(relx=0.65, rely=0.467, relheight=0.04, relwidth=0.122)
                self.Persistance.configure(background="#d9d9d9",
                                        foreground="#000000",
                                        highlightbackground="#d9d9d9",
                                        highlightcolor="black",
                                        text='''Persistance :''',
                                        width=73
                                        )

                self.Lacunarity = tk.Message(top)
                self.Lacunarity.place(relx=0.65, rely=0.556, relheight=0.029
                        , relwidth=0.115)
                self.Lacunarity.configure(background="#d9d9d9",
                                        foreground="#000000",
                                        highlightbackground="#d9d9d9",
                                        highlightcolor="black",
                                        text='''Lacunarity :''',
                                        width=69)
                                
                self.Threshold = tk.Message(top)
                self.Threshold.place(relx=0.667, rely=0.644, relheight=0.051
                        , relwidth=0.1)
                self.Threshold.configure(background="#d9d9d9",
                                        foreground="#000000",
                                        highlightbackground="#d9d9d9",
                                        highlightcolor="black",
                                        text='''Threshold :''',
                                        width=60)

                self.Xposition= tk.Entry(top, textvariable=PositionX)
                PositionX.set(100)
                self.Xposition.place(relx=0.783, rely=0.111, height=20, relwidth=0.073)
                self.Xposition.configure(background="white",
                                        disabledforeground="#a3a3a3",
                                        highlightcolor="black",
                                        insertbackground="black",
                                        selectbackground="blue",
                                        selectforeground="white",
                                        font="TkFixedFont",
                                        foreground="#000000",
                                )

                self.Yposition= tk.Entry(top, textvariable=PositionY)
                PositionY.set(100)
                self.Yposition.place(relx=0.883, rely=0.111, height=20, relwidth=0.073)
                self.Yposition.configure(background="white",
                                        disabledforeground="#a3a3a3",
                                        font="TkFixedFont",
                                        foreground="#000000",
                                        highlightbackground="#d9d9d9",
                                        highlightcolor="black",
                                        insertbackground="black",
                                        selectbackground="blue",
                                        selectforeground="white",
                                )

                self.Color_range_entry = tk.Entry(top, textvariable=Color_range)
                Color_range.set(10)
                self.Color_range_entry.place(relx=0.783, rely=0.2, height=20, relwidth=0.107)
                self.Color_range_entry.configure(background="white",
                                                disabledforeground="#a3a3a3",
                                                font="TkFixedFont",
                                                foreground="#000000",
                                                highlightbackground="#d9d9d9",
                                                highlightcolor="black",
                                                insertbackground="black",
                                                selectbackground="blue",
                                                selectforeground="white",
                                        )

                self.Scale_entry = tk.Entry(top, textvariable=Scale)
                Scale.set(350)
                self.Scale_entry.place(relx=0.783, rely=0.289, height=20, relwidth=0.107)
                self.Scale_entry.configure(background="white",
                                        disabledforeground="#a3a3a3",
                                        font="TkFixedFont",
                                        foreground="#000000",
                                        highlightbackground="#d9d9d9",
                                        highlightcolor="black",
                                        insertbackground="black",
                                        selectbackground="blue",
                                        selectforeground="white",
                                        )

                self.Persistence_entry = tk.Entry(top, textvariable=Persistence)
                Persistence.set(0.6)
                self.Persistence_entry.place(relx=0.783, rely=0.467, height=20, relwidth=0.107)
                self.Persistence_entry.configure(background="white",
                                                disabledforeground="#a3a3a3",
                                                font="TkFixedFont",
                                                foreground="#000000",
                                                highlightbackground="#d9d9d9",
                                                highlightcolor="black",
                                                insertbackground="black",
                                                selectbackground="blue",
                                                selectforeground="white",
                                                )

                self.Lacunarity_entry = tk.Entry(top, textvariable=Lacunarity)
                Lacunarity.set(3.0)
                self.Lacunarity_entry.place(relx=0.783, rely=0.556, height=20, relwidth=0.107)
                self.Lacunarity_entry.configure(background="white",
                                                disabledforeground="#a3a3a3",
                                                font="TkFixedFont",
                                                foreground="#000000",
                                                highlightbackground="#d9d9d9",
                                                highlightcolor="black",
                                                insertbackground="black",
                                                selectbackground="blue",
                                                selectforeground="white",
                                        )

                self.Octaves_entry = tk.Entry(top, textvariable=Octaves)
                Octaves.set(10)
                self.Octaves_entry.place(relx=0.783, rely=0.378, height=20, relwidth=0.107)
                self.Octaves_entry.configure(background="white",
                                        disabledforeground="#a3a3a3",
                                        font="TkFixedFont",
                                        foreground="#000000",
                                        highlightbackground="#d9d9d9",
                                        highlightcolor="black",
                                        insertbackground="black",
                                        selectbackground="blue",
                                        selectforeground="white",
                                        )

                self.Threshold_entry = tk.Entry(top, textvariable=threshold)
                threshold.set(-0.09)
                self.Threshold_entry.place(relx=0.783, rely=0.644, height=20, relwidth=0.107)
                self.Threshold_entry.configure(background="white",
                                               disabledforeground="#a3a3a3",
                                               font="TkFixedFont",
                                               foreground="#000000",
                                               highlightbackground="#d9d9d9",
                                               highlightcolor="black",
                                               insertbackground="black",
                                               selectbackground="blue",
                                               selectforeground="white",
                                        )

                # get result of the image
                get_result = partial(get_call, PositionX, PositionY, Color_range, Scale, Octaves, Persistence, Lacunarity, threshold)

                self.Generate_button = tk.Button(top, command=self.combineFunc(get_result, lambda:update_image(self)))
                self.Generate_button.place(relx=0.667, rely=0.867, height=24, width=77)
                self.Generate_button.configure(activebackground="#ececec",
                                        activeforeground="#000000",
                                        background="#d9d9d9",
                                        disabledforeground="#a3a3a3",
                                        foreground="#000000",
                                        highlightbackground="#d9d9d9",
                                        highlightcolor="black",
                                        pady="0",
                                        text='''Generate''',)

                self.Save_button = tk.Button(top, command=lambda:save(path="gui_beta/output", filetype="png"))
                self.Save_button.place(relx=0.85, rely=0.867, height=24, width=67)
                self.Save_button.configure(activebackground="#ececec",
                                        activeforeground="#000000",
                                        background="#d9d9d9",
                                        disabledforeground="#a3a3a3",
                                        foreground="#000000",
                                        highlightbackground="#d9d9d9",
                                        highlightcolor="black",
                                        pady="0",
                                        text='''Save''',)

                self.Text_Logo = tk.Message(top)
                self.Text_Logo.place(relx=0.017, rely=0.867, relheight=0.051
                        , relwidth=0.15)
                        
                self.Text_Logo.configure(background="#d9d9d9",
                                        foreground="#000000",
                                        highlightbackground="#d9d9d9",
                                        highlightcolor="black",
                                        text='''© Projeckt_Map''',
                                        width=90)

                def update_image(self, *args, **kwargs):
                        self.update_img = ImageTk.PhotoImage(Image.open('lib/bin/result_veg.jpeg'))
                        self.Preview_Image.itemconfig(self.image_id, image=self.update_img)

                def save(path, filetype):
                        file_name = str(uuid.uuid4())
                        img = Image.open('bin/result_veg.jpeg')
                        fullpath = os.path.join(path, file_name + '.' + filetype)
                        img.save(fullpath)
                        print("Saved")
                        
        # Multi-threading
        def combineFunc(self, *funcs):
                def combinedFunc(*args, **kwargs):
                        for f in funcs:
                                f(*args, **kwargs)
                return combinedFunc
if __name__ == '__main__':
    vp_start_gui()

