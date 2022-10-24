# -*- coding: utf-8 -*-

from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from plyer import camera

kv = """
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
                            
        Widget:
"""

class MyApp(MDApp):

    def build(self):
        return Builder.load_string(kv)


if __name__ == '__main__':
    MyApp().run()
    Window.close()