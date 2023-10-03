import PySimpleGUI as sg
from zipcreator import archive
label1 = sg.Text("Select files to compress:")
input1 = sg.Input()
button1 = sg.FilesBrowse("Choose", key='files')


label2 = sg.Text("Select destination folder:")
input2 = sg.Input()
button2 = sg.FolderBrowse("Choose", key='desfolder')
compress_button = sg.Button("Compress")
output = sg.Text(key="output",text_color="green")
window = sg.Window("File Compressor", layout=[[label1, input1, button1],
[label2,input2,button2 ], [compress_button,output]])

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Exit":
        break
    elif event == "Compress":
        filepath = values["files"].split(";")
        folderpath = values["desfolder"]
        archive(filepath, folderpath)
        window["output"].update(value="Compression completed")


window.close()
