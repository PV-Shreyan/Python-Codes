# Design Counter App (This app has a button that increments a counter 
# displayed on the screen every time the button is clicked)

# Importing necessary modules from kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

# Defining the main application class
class CounterApp(App):
    def build(self):
        # Creating a layout
        layout = BoxLayout(orientation='vertical')
        
        self.counter = 0
        
        # Creating a label and adding it to the layout
        self.label = Label(text=f"Counter: {self.counter}", font_size=32)
        layout.add_widget(self.label)
        
        # Creating a button and binding it to the counter function
        button = Button(text="Press to Increment", font_size=24)
        button.bind(on_press=self.increment_counter)
        layout.add_widget(button)
        
        return layout
    
    # Function to increment counter and update label
    def increment_counter(self, instance):
        self.counter += 1
        self.label.text = f"Counter: {self.counter}"

# Running the application
if __name__ == '__main__':
    CounterApp().run()
    
