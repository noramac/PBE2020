import gi
import lcddriver
display = lcddriver.lcd()

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Pango


class TextViewWindow(Gtk.Window):   #Defineix la finestra i li posa el texview i el boto.
    def __init__(self):
        Gtk.Window.__init__(self, title="Lcd raspberry")

        self.set_default_size(350, 120)

        self.grid = Gtk.Grid()
        self.add(self.grid)
        
        self.create_textview()
        self.create_buttons()

    
    def create_textview(self):  #Crea el texview i mostra un text amb instruccions dins
        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.set_hexpand(True)
        scrolledwindow.set_vexpand(True)
        self.grid.attach(scrolledwindow, 0, 1, 3, 1)

        self.textview = Gtk.TextView()
        self.textbuffer = self.textview.get_buffer()
        self.textbuffer.set_text(
            "Insereix aqui el que vols" + "\n" +"que es mostri al display"
            + "\n" + "i clica display" + "\n" + "max 20 car/linia"
        )
        scrolledwindow.add(self.textview)
        self.tag_found = self.textbuffer.create_tag("found", background="yellow")

    def create_buttons(self):   #Crea el botó a baix de la finestra 
        button = Gtk.Button.new_with_label("Display")
        button.connect("clicked", self.on_click_me_clicked)
        self.grid.attach(button, 0, 2, 3, 1)

    def lcd_print(self,total):#mostra string de 4 linies a la pantalla
        linex = 1
        for x in total:
            display.lcd_display_string(x, linex)
            linex += 1

    def prepara_text(self): #prepara el text per la funcio lcd_print i dona error quan el text o es valid 
        start_iter = self.textbuffer.get_start_iter()
        end_iter = self.textbuffer.get_end_iter()
        text = self.textbuffer.get_text(start_iter, end_iter, True)
        total = text.split("\n",4)
        for line in total:
            if len(line) > 20:
                self.error_text()
                del total[:]
                break
        return total

    def on_click_me_clicked(self, button):#Quan es clica el boto s'envia el text al lcd
        total = self.prepara_text()
        self.lcd_print(total)

    def error_text(self):   #misstge d'error
        dialog = Gtk.MessageDialog(
            transient_for=self,
            flags=0,
            message_type=Gtk.MessageType.ERROR,
            buttons=Gtk.ButtonsType.OK,
            text="Text no vàlid",
        )
        dialog.format_secondary_text(
            "Màxim 20 caracters per linia"
        )
        dialog.run()
        dialog.destroy()
    
win = TextViewWindow()
win.set_position(Gtk.WindowPosition.CENTER)
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
