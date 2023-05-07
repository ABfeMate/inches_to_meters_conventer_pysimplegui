import PySimpleGUI as sg

feet_label = sg.Text("Enter feet:")
feet_input = sg.Input(key="feet")

inches_label = sg.Text("Enter inches:")
inches_input = sg.Input(key="inches")

convert_button = sg.Button("Convert", key="convert")
output_label = sg.Text(key="output")

window = sg.Window("Feet and Inches to Meters Converter",
                   layout=[[feet_label, feet_input],
                           [inches_label, inches_input],
                           [convert_button, output_label]])


def get_meters(feet=0, inches=0):
    total_inches = feet * 12 + inches
    meters = round(total_inches * 0.0254, 3)

    return meters


while True:
    event, values = window.read()
    print(event, values)

    if event == sg.WIN_CLOSED:
        break

    feet_str = values["feet"].strip()
    inches_str = values["inches"].strip()

    try:
        feet = float(feet_str) if feet_str else 0.0
        inches = float(inches_str) if inches_str else 0.0

        total_meters = get_meters(feet, inches)

        window["output"].update(value=f"{total_meters} m")
    except ValueError:
        window["output"].update(value="Invalid input. Please enter numbers for feet and inches.")

window.close()
