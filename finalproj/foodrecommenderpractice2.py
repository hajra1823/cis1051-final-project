import kivy
import random
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image

#printplace = ''
foodlist = []
# SCREEN ONE:

class ScreenOne(Screen):

    def __init__ (self,**kwargs):
        super (ScreenOne, self).__init__(**kwargs)

        # ADDING STRUCTURAL ELEMENTS

        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # CREATING IMAGE, INPUT TEXTBOX, AND BUTTONS

        my_image = Image(
            source = 'foodtruck.png',
            pos_hint = {'center_x': 0.5, 'center_y': 0.8},
            size_hint = (0.5, 0.5),
            size_hint_y = None
        )

        my_box1 = BoxLayout(orientation='vertical')
        self.greeting = Label(
            text = "What food place\ndo you want?", 
            font_size = '24dp',
            font_name = "Neutro-ExtraBold.otf",
            halign = 'center')
            #size_hint = (0.6, 0.3))


        addinput = TextInput(
            multiline = False, 
            padding_x = (20, 0),
            size_hint = (0.6, 0.3),
            pos_hint = {'x': 0.2, 'y': 0.2},
            padding_y = (20, 20),
            font_name = "FRAMD")
        

        buttonadd = Button(
            text = "ADD",
            size_hint = (0.6, 0.2),
            pos_hint = {'x': 0.2, 'y': 0.2},
            bold = True,
            background_color = "579e82", 
            background_normal = "",
            font_name = "Neutro-ExtraBold.otf"
        )

        buttonswitch = Button(
            text = "DONE",
            size_hint_y = None,
            size_hint = (0.6, 0.2),
            background_color = "ba5959",
            background_normal = "",
            font_name = "Neutro-ExtraBold.otf",
            pos_hint = {'x': 0.2, 'y': 0.2},
            
            )


        # SPACERS

        spacer0 = Label(size_hint_y = 0.2)
        spacer1 = Label(size_hint_y = 0.2)
        spacer2 = Label(size_hint_y = 0.1)
        spacer3 = Label(size_hint_y = 0.2)

        # ADDING WIDGETS TO THE SCREEN

        my_box1.add_widget(spacer0)
        my_box1.add_widget(my_image)
        self.add_widget(my_box1)
        my_box1.add_widget(self.greeting)
        my_box1.add_widget(addinput)
        my_box1.add_widget(spacer1)

        my_box1.add_widget(buttonadd)

        my_box1.add_widget(spacer2)

        my_box1.add_widget(buttonswitch)
        my_box1.add_widget(spacer3)


        # BINDING BUTTONS

        buttonswitch.bind(on_press = self.changer)

        foodlist = []

        def addfood(addinput):

            global foodlist

            addinput = str(addinput.text)
            foodlist.append(addinput)
            print(foodlist)
            return foodlist

        buttonadd.bind(on_press = lambda x: addfood(addinput))
        
    # SWITCH TO SCREEN TWO

    def changer(self,*args):
        self.manager.current = 'screen2'




# SCREEN TWO:

class ScreenTwo(Screen):

    def __init__(self,**kwargs):
        super (ScreenTwo,self).__init__(**kwargs)

        printplace = Label(
                text = 'foodplace'
            )

        # GENERATE A FOOD PLACE

        def generate(foodlist):

            global printplace

            foodplace = random.choice(foodlist)
            printplace = Label(
                text = foodplace,
                font_size='24dp',
                font_name = "FRAMD")
            my_box1.add_widget(printplace)
            return printplace

        # CREATING TEXT AND BUTTONS

        my_box1 = BoxLayout(orientation='vertical')
        my_label1 = Label(text = 
        "Your food\nrecommendation is...",
        font_size='24dp',
        font_name = "Neutro-ExtraBold.otf",
        halign = 'center')

        buttongenerate = Button(
            text = "GENERATE",
            size_hint = (0.6, 0.2),
            pos_hint = {'x': 0.2, 'y': 0.2},
            bold = True,
            background_color = "579e82", 
            background_normal = "",
            font_name = "Neutro-ExtraBold.otf"
        )
        
        my_label2 = Label(text = 
        #generate(foodlist),
        'example food place',
        font_size='24dp',
        font_name = "FRAMD")

        #my_foodlist = Label( text = init)
        my_button1 = Button(
            text = "GO BACK",
            size_hint = (0.6, 0.2),
            pos_hint = {'x': 0.2, 'y': 0.2},
            bold = True,
            background_color = "579e82", 
            background_normal = "",
            font_name = "Neutro-ExtraBold.otf"
        )

        buttonexit = Button(
            text = "EXIT",
            size_hint = (0.6, 0.2),
            pos_hint = {'x': 0.2, 'y': 0.2},
            bold = True,
            background_color = "ba5959", 
            background_normal = "",
            font_name = "Neutro-ExtraBold.otf"
        )

        # BINDING BUTTONS

        my_button1.bind(on_press = self.changer)
        buttongenerate.bind(on_press = lambda x: generate(foodlist))
        #buttonexit.bind(on_press = app.stop())
        #buttonexit.bind(on_press = App.get_running_app().stop())


        # SPACERS

        spacer4 = Label(size_hint_y = 0.2)
        spacer5 = Label(size_hint_y = 0.2)


        # ADDING WIDGETS TO THE SCREEN

        my_box1.add_widget(my_label1)
        my_box1.add_widget(buttongenerate)
        my_box1.add_widget(my_label2)
        my_box1.add_widget(my_button1)
        my_box1.add_widget(spacer5)
        my_box1.add_widget(printplace)

        #my_box1.add_widget(buttonexit)
        self.add_widget(my_box1)
        my_box1.add_widget(spacer4)

    # SWITCH BACK TO SCREEN ONE

    def changer(self,*args):
        self.manager.current = 'screen1'


# PUTTING EVERYTHING TOGETHER 

class Foody(App):

    def build(self):
        my_screenmanager = ScreenManager()
        screen1 = ScreenOne(name = 'screen1')
        screen2 = ScreenTwo(name = 'screen2')
        my_screenmanager.add_widget(screen1)
        my_screenmanager.add_widget(screen2)
        return my_screenmanager

if __name__ == '__main__':
    Foody().run()
