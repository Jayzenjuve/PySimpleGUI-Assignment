import PySimpleGUI as sg 
sg.theme("DarkTeal12")
window = sg.Window(title="Profile", 
  layout=[[sg.Text("NPM      : 2210010125")],
          [sg.Text("Nama     : Trimuldiyanto Wijaya")],
          [sg.Text("Kelas    : 5N Reguler Banjarmasin")],
          [sg.Text("Matkul   : Pemrograman Visual 3")] 
         ],
  size=(400,200))
window()
window.close()