from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.storage.jsonstore import JsonStore

Builder.load_string("""
<MenuScreen>:
    FloatLayout:
        Button:
            text: 'Credit'
            size_hint: None, None
            size: 80, 50
            pos_hint: {'x': 0.3, 'y':0.5}
            on_press: root.manager.current = 'credit'
        Button:
            text: 'Debit'
            size_hint: None, None
            size: 80, 50
            pos_hint: {'x': 0.5, 'y':0.5}
            on_press: root.manager.current = 'debit'
        Button:
            text: 'Quit'
            size_hint: None, None
            size: 70, 50
            pos_hint: {'x': 0.7, 'y':0.5}   
            on_press: app.close_app()
                

<CreditScreen>:
    FloatLayout:
        
        Label:
            text: 'Credit Amount:'
            pos_hint: {'x': -0.25, 'y':0.225}
                    
        TextInput:
            id: credit
            font_size: 20
            size_hint: .3, .05
            pos_hint: {'x': 0.35, 'y':0.7}
            multiline: False
            input_filter: 'float'
        
        Label:
            text: 'Credit Date:'
            pos_hint: {'x': -0.25, 'y':0.125}
                    
        TextInput:
            id: creditd
            font_size: 20
            size_hint: .3, .05
            pos_hint: {'x': 0.35, 'y':0.6}
            multiline: False
            input_filter: 'float'
                    
        Button:
            text: 'Back to menu'
            size_hint: None, None
            size: 120, 50
            pos_hint: {'x': 0.44, 'y':0.2}
            on_press: root.manager.current = 'menu'

<DebitScreen>:
    FloatLayout:
        
        Label:
            text: 'Debit Amount:'
            pos_hint: {'x': -0.25, 'y':0.225}
                    
        TextInput:
            id: debit
            font_size: 20
            size_hint: .3, .05
            pos_hint: {'x': 0.35, 'y':0.7}
            multiline: False
            input_filter: 'float'
        
        Label:
            text: 'Debit Date:'
            pos_hint: {'x': -0.25, 'y':0.125}
                    
        TextInput:
            id: debitd
            font_size: 20
            size_hint: .3, .05
            pos_hint: {'x': 0.35, 'y':0.6}
            multiline: False
            input_filter: 'float'
                    
        Button:
            text: 'Back to menu'
            size_hint: None, None
            size: 120, 50
            pos_hint: {'x': 0.44, 'y':0.2}
            on_press: root.manager.current = 'menu'   
""")

class MenuScreen(Screen):
    pass

class CreditScreen(Screen):
    pass

class DebitScreen(Screen):
    pass

store = JsonStore('expenses.json')

class TestApp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(CreditScreen(name='credit'))
        sm.add_widget(DebitScreen(name='debit'))

        return sm
    def close_app(self):
        App.get_running_app().stop()
        Window.close()

if __name__ == '__main__':
    TestApp().run()