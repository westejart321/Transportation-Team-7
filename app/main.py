import kivy
import gspread
from oauth2client.service_account import ServiceAccountCredentials
kivy.require("1.11.1")
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
class MyApp(App):


    def build(self):
        client = gspread.service_account('Bus tracking.json') #connecting to the sheets database
        sheet = client.open('bus').sheet1
        print(sheet.acell('A1').value)
        def ShowInfo(instance): #shows info for the bus
            bus = busInput.text
            listOfBus = sheet.col_values(1)
            rowNum = -1
            count = 1;
            for num in listOfBus: #searches for the bus number in the database
                if bus == num:
                    rowNum = count
                count+=1
            if rowNum == -1:
                textLabel.text = 'Not a valid bus, please enter a different bus number'
                busInput.text = ''
            else:
                root.clear_widgets() #switching screens
                riders = sheet.acell('B' + str(rowNum)).value #prepping the strings
                capacity = sheet.acell('C' + str(rowNum)).value
                time = sheet.acell('D' + str(rowNum)).value
                route = sheet.acell('E' + str(rowNum)).value
                text = 'Bus ' + str(bus) + ' on route ' + route + ' currently has ' + str(riders) + ' riders on it \nLast measured at ' + str(time)
                root.add_widget(Label(text=text))
                if (riders >= capacity): #displays if bus it over capacity
                    root.add_widget(Label(text = 'This bus is currently at capacity we recommend switching to a different bus'))
                root.add_widget(backButton)
        def Return(instance): #resets the app to the landing page
            root.clear_widgets()
            textLabel.text = 'Please Enter Bus Number'
            root.add_widget(textLabel)
            root.add_widget(busInput)
            busInput.text=''
            root.add_widget(enterButton)

        root = GridLayout(rows=3) #setup for the landing page
        textLabel = Label(text='Please Enter Bus Number')
        busInput = TextInput(halign='center',multiline=False)
        enterButton = Button(text='Enter')
        enterButton.bind(on_press=ShowInfo)
        backButton = Button(text='Return')
        backButton.bind(on_press=Return)
        root.add_widget(textLabel)
        root.add_widget(busInput)
        root.add_widget(enterButton)

        return root

if __name__ == '__main__':
    MyApp().run()