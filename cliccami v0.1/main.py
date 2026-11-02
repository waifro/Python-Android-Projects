# 1. IMPORTAZIONE DEI MODULI
import pathlib
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


def init_create_file(filename, num):
    
    data = 0
    if data != num:
        data = num

    f_path = pathlib.Path(filename)
        
    if f_path.exists():
        f_path = open(filename, "r")
        data = int(f_path.read())
    else:
        with open(filename, "w") as f_path:
            f_path = open(filename, "w")
            f_path.write(str(data))
    
    return data

def init_update_file(filename, num):
    
    data = num + 1

    with open(filename, "w") as f_path:
        f_path = open(filename, "w")
        f_path.write(str(data))
    
    return data

# 2. DEFINIZIONE DELLA TUA INTERFACCIA (WIDGET / LAYOUT)
class MiaInterfaccia(BoxLayout):
    
    # primissima funzione che Python fa girare nella chiamata della classe
    def __init__(self, data, **kwargs):
        super(MiaInterfaccia, self).__init__(**kwargs)
        
        # Impostiamo il layout verticale
        self.valore_attuale = data
        self.orientation = 'vertical'
        self.padding = 50
        self.spacing = 20

        # Aggiungiamo un'etichetta (Testo)
        self.label_titolo = Label(
            text=str(self.valore_attuale),
            font_size=24,
            size_hint=(1, 0.5)
        )
        self.add_widget(self.label_titolo)

        # Aggiungiamo un bottone interattivo
        self.bottone = Button(
            text="Cliccami",
            font_size=20,
            size_hint=(1, 0.5)
        )
        # Colleghiamo il click del bottone a una funzione
        self.bottone.bind(on_press=self.on_button_click)
        self.add_widget(self.bottone)

    # 3. LOGICA DELL'APPLICAZIONE (FUNZIONI)
    def on_button_click(self, instance):
        self.valore_attuale = init_update_file("cliccami.txt", self.valore_attuale)
        self.label_titolo.text = str(self.valore_attuale)


# 4. LA CLASSE PRINCIPALE DELL'APPLICAZIONE
class MiaApp(App):
    def build(self):
        
        #creiamo il file
        data = init_create_file("cliccami.txt", 0)
        
        return MiaInterfaccia(data=data)


# 5. PUNTO DI INGRESSO (ENTRY POINT)
if __name__ == '__main__':
    MiaApp().run()