import PySimpleGUI as sg 
sg.theme("DarkTeal12")
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Profile", 
                   layout=[[sg.Text("SELAMAT DATANG DI KELAS",
                                    font=("Arial", 25,"italic","bold","underline"))],
                           [sg.Text("NPM      : 2210010125")],
                           [sg.Text("Nama     : Trimuldiyanto Wijaya")],
                           [sg.Text("Kelas    : 5N Reguler Banjarmasin")]
                          ],
                    size=(510,200),
                    font=("Times", 18))
window()
window.close()