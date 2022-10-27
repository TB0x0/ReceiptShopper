# -*- coding: utf-8 -*-

from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from plyer import camera

import os

Builder.load_string("""
Screen:
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "MDToolbar"
            left_action_items: [["menu", lambda x: nav_draw.set_state()]]
        Widget:
                    
    MDNavigationDrawer:
        id: nav_draw
        orientation: "vertical"
        padding: "8dp"
        spacing: "8dp"
        
        AnchorLayout:
            anchor_x: "left"
            size_hint_y: None
            height: avatar.height
            Image:
                id: avatar
                size_hint: None, None
                size: "56dp", "56dp"
                source: "data/logo/kivy-icon-256.png"
        MDLabel:
            text: "Receipt Shopper Pro"
            font_style: "Button"
            size_hint_y: None
            height: self.texture_size[1]
    
        MDLabel:
            text: "rppadmin@gmail.com"
            font_style: "Caption"
            size_hint_y: None
            height: self.texture_size[1]
        
        ScrollView:
            MDList:
                OneLineAvatarListItem:
                    on_press:
                        nav_draw.set_state("close")
                    text: "Home"
                    IconLeftWidget:
                        icon: "home"
                OneLineAvatarListItem:
                    on_press:
                        nav_draw.set_state("close")
                    text: "About"
                    IconLeftWidget:
                        icon: 'information'
                            
       <MyWidget>:
    id: my_widget
    Button
        text: "open"
        on_release: my_widget.open(filechooser.path, filechooser.selection)
    FileChooserListView:
        id: filechooser
        on_selection: my_widget.selected(filechooser.selection)
""")

class MyWidget(BoxLayout):
    def open(self, path, filename):
        with open(os.path.join(path, filename[0])) as f:
            print(f.read())

    def selected(self, filename):
        print("selected: %s" % filename[0])



class MyApp(MDApp):

    def build(self):
        return Builder.load_string(kv)


if __name__ == '__main__':
    MyApp().run()
    Window.close()