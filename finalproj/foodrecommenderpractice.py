
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class FoodPlacr(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        
        #add widgets to window


        # image widget (ADD LATER)
        #self.window.add_widget(Image(source = ))

        self.greeting = Label(
                        text = "What food place do you want?",
                        font_size = 20,
                        color = "00FFCE"
                        )
        self.window.add_widget(self.greeting)

        self.user = TextInput(
                    multiline = False,
                    padding_y = (20, 20),
                    size_hint = (1, 0.5)
                    )
            
           
        self.window.add_widget(self.user)

        

        #button widget
        self.button = Button(
                    text = "ADD",
                    size_hint = (1, 0.5),
                    bold = True,
                    background_color = "00FFCE", 
                    background_normal = "")

        self.button.bind(on_press = self.callback)
        self.window.add_widget(self.button)

        self.button = Button(
                    text = "DONE",
                    size_hint = (1, 0.5),
                    bold = True,
                    background_color = "green", 
                    background_normal = "")

        self.button.bind(on_press = self.callback)
        self.window.add_widget(self.button)



        return self.window

    


    def callback(self, instance):
        # while not done:
        #     add InputS
        #     add a second button that says done
        #     print random suggestion
        foodlist = []

        self.greeting.text = "Mm, mm , mm.... " + self.user.text + ". YUM!"
        foodlist = foodlist.append(self.user.text)
        print(foodlist)


if __name__ == "__main__":
    FoodPlacr().run()
    


