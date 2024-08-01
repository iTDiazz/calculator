from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.boxlayout import MDBoxLayout


class BoxApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Purple"

        def press_but(self):
            nonlocal label
            if self.text == "=":
                label.text = str(eval(label.text))
            elif self.text == "C":
                label.text = ""
            else:
                label.text += self.text

        b1 = MDBoxLayout(orientation="vertical", padding=100)
        label = MDLabel(halign="right", text="", font_style="H2")
        b1.add_widget(label)

        buttons = [["7", "8", "9", "/"],
                   ["4", "5", "6", "*"],
                   ["1", "2", "3", "-"],
                   ["0", ".", "C", "+"],
                   ["="]]

        for i in buttons:
            vr = MDBoxLayout()
            for j in i:
                if j == "=":
                    but = MDRectangleFlatButton(text=j,
                                                size_hint=(1, 1),
                                                font_size=50,
                                                md_bg_color=(0, 1, 0, 0.02),
                                                on_press=press_but)
                else:
                    but = MDRectangleFlatButton(text=j,
                                                size_hint=(1 / len(i), 1),
                                                font_size=50,
                                                md_bg_color=(0, 1, 0, 0.02),
                                                on_press=press_but)
                vr.add_widget(but)
            b1.add_widget(vr)

        return b1


BoxApp().run()