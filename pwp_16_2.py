# Text Input App (This app allows users to type in a text field and display 
# the typed text on the screen when a button is pressed.)

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

# Defining the main application class
class TextInputApp(App):
    def build(self):
        # Main layout
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Input label
        self.input_label = Label(text="Enter some text:")
        layout.add_widget(self.input_label)
        
        # Text input field
        self.text_input = TextInput(multiline=False)
        layout.add_widget(self.text_input)
        
        # Display button
        self.display_button = Button(text="Display Text")
        self.display_button.bind(on_press=self.display_text)
        layout.add_widget(self.display_button)
        
        # Label to show the entered text
        self.output_label = Label(text="")
        layout.add_widget(self.output_label)
        
        return layout
    
    # Function to display typed text
    def display_text(self, instance):
        entered_text = self.text_input.text
        self.output_label.text = f"You entered: {entered_text}"

# Running the application
if __name__ == '__main__':
    TextInputApp().run()
