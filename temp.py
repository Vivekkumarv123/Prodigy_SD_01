import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Conversion functions
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return fahrenheit_to_celsius(f) + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return celsius_to_fahrenheit(kelvin_to_celsius(k))

def convert_temperature():
    try:
        temp_value = float(temp_entry.get())
        original_unit = unit_var.get()
        
        if original_unit == 'Celsius':
            fahrenheit = celsius_to_fahrenheit(temp_value)
            kelvin = celsius_to_kelvin(temp_value)
            celsius = temp_value
        elif original_unit == 'Fahrenheit':
            celsius = fahrenheit_to_celsius(temp_value)
            kelvin = fahrenheit_to_kelvin(temp_value)
            fahrenheit = temp_value
        elif original_unit == 'Kelvin':
            celsius = kelvin_to_celsius(temp_value)
            fahrenheit = kelvin_to_fahrenheit(temp_value)
            kelvin = temp_value
        
        result_label.config(text=f'Celsius: {celsius:.2f} °C\nFahrenheit: {fahrenheit:.2f} °F\nKelvin: {kelvin:.2f} K')
    
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for the temperature.")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("600x500")
root.configure(bg='#f0f8ff')

# Font and style
font_name = 'Comic Sans MS'

# Frame for input
input_frame = ttk.Frame(root, padding="20 20 20 20", style='Custom.TFrame')
input_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Temperature input
temp_label = ttk.Label(input_frame, text="Enter Temperature:", font=(font_name, 14), background='#add8e6')
temp_label.grid(column=0, row=0, padx=10, pady=10, sticky=tk.W)

temp_entry = ttk.Entry(input_frame, width=20, font=(font_name, 14))
temp_entry.grid(column=1, row=0, padx=10, pady=10)

# Unit selection
unit_label = ttk.Label(input_frame, text="Select Unit:", font=(font_name, 14), background='#add8e6')
unit_label.grid(column=0, row=1, padx=10, pady=10, sticky=tk.W)

unit_var = tk.StringVar()
unit_combobox = ttk.Combobox(input_frame, textvariable=unit_var, font=(font_name, 14))
unit_combobox['values'] = ('Celsius', 'Fahrenheit', 'Kelvin')
unit_combobox.grid(column=1, row=1, padx=10, pady=10)
unit_combobox.current(0)

# Convert button
convert_button = ttk.Button(input_frame, text="Convert", command=convert_temperature )
convert_button.grid(column=0, row=2, columnspan=2, pady=20)

# Result display
result_label = ttk.Label(root, text="", padding="20 20 20 20", font=(font_name, 14), background='#f0f8ff')
result_label.grid(column=0, row=1, sticky=(tk.W, tk.E))

# Configure the grid to be responsive
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
input_frame.columnconfigure(1, weight=1)

# Style
style = ttk.Style()
style.configure('TButton', font=(font_name, 14))
style.configure('Accent.TButton', font=(font_name, 14, 'bold'), background='#ff69b4', foreground='#ffffff')
style.configure('TFrame', background='#f0f8ff')
style.configure('Custom.TFrame', background='#add8e6')

# Run the main loop
root.mainloop()
