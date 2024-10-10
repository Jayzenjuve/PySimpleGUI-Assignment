import PySimpleGUI as sg 
sg.theme("DarkRed1")
sg.theme_text_color("#0000FF")
sg.theme_text_element_background_color("azure4")
window = sg.Window(title="Profile", 
                   layout=[[sg.Text("NPM      : 2210010125")],
                           [sg.Text("Nama     : Trimuldiyanto Wijaya")],
                           [sg.Text("Kelas    : 5N Reguler Banjarmasin")],
                           [sg.Text("Matkul   : Pemrograman Visual 3")] 
                          ],
                    size=(400,200))
window()
window.close()