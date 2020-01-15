from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class loginForm(App):
    
     def build(self):

        order = BoxLayout(orientation='vertical')

        order.add_widget(Label(text="User's Name  "))
        userName = TextInput()        
        order.add_widget(userName)

        order.add_widget(Label(text=("User's Password  ")))
        userPassword = TextInput()
        order.add_widget(userPassword)

        order.add_widget(Widget())
        enterButton = Button(text="Login")
        order.add_widget(enterButton)
        self.title = "User's Login Page "

        return order


loginForm().run()
