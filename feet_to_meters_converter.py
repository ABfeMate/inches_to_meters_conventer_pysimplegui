import PySimpleGUI as sg

# Setting the theme for PySimpleGUI
sg.theme("Black")


def get_meters(feet=0, inches=0):
    total_inches = feet * 12 + inches
    meters = round(total_inches * 0.0254, 3)
    return meters


def get_feet_inches(meters=0):
    total_inches = meters / 0.0254
    feet = int(total_inches // 12)
    inches = round(total_inches % 12, 3)
    return feet, inches


# Layout elements
label_feet = sg.Text("Enter feet:", key="label_feet")
input_feet = sg.Input(key="input_feet")

label_inches = sg.Text("Enter inches:", key="label_inches")
input_inches = sg.Input(key="input_inches")

convert_button = sg.Button("Convert", key="convert")
toggle_button = sg.Button("Toggle", key="toggle")
conversion_label = sg.Text("Feet & Inches to Meters", key="conversion_mode_label")

exit_button = sg.Button("Exit", key="exit")
output_label = sg.Text(key="output", size=(60, 1))

layout = [
    [label_feet, input_feet],
    [label_inches, input_inches],
    [convert_button, toggle_button, conversion_label],
    [output_label, exit_button]
]

window = sg.Window("Length Converter", layout)

conversion_mode = "to_meters"

while True:
    event, values = window.read()
    print(event, values)

    if event == sg.WIN_CLOSED or event == "exit":
        break

    try:
        if event == "convert":
            value1_str = values["input_feet"].strip()
            value2_str = values["input_inches"].strip()
            value1 = float(value1_str) if value1_str else 0.0
            value2 = float(value2_str) if value2_str else 0.0

            if conversion_mode == "to_meters":
                total_meters = get_meters(value1, value2)
                window["output"].update(value=f"{total_meters} m")
            else:
                meters = value1 + value2 / 100
                feet, inches = get_feet_inches(meters)
                window["output"].update(value=f"{feet} ft {inches} in")

        elif event == "toggle":
            if conversion_mode == "to_meters":
                window["conversion_mode_label"].update("Meters to Feet & Inches")
                conversion_mode = "to_feet_inches"
                window["input_feet"].update(value="")
                window["input_inches"].update(value="")
                window["output"].update(value="")
                window["label_feet"].Update("Enter meters:")
                window["label_inches"].Update("Enter centimeters:")
            else:
                window["conversion_mode_label"].update("Feet & Inches to Meters")
                conversion_mode = "to_meters"
                window["input_feet"].update(value="")
                window["input_inches"].update(value="")
                window["output"].update(value="")
                window["label_feet"].Update("Enter feet:")
                window["label_inches"].Update("Enter inches:")
    except ValueError:
        window["output"].update(value="Invalid input. Please enter numbers for values.")

window.close()