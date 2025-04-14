import tkinter as tk
from tkinter import messagebox

# Function to calculate BMI
def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height_cm = float(entry_height.get())
        height_m = height_cm / 100
        bmi = round(weight / (height_m ** 2), 2)

        # Determine BMI category
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 25:
            category = "Normal"
        elif 25 <= bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(
            text=f"BMI: {bmi}\nCategory: {category}",
            fg="white", bg="#444"
        )
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

# Function to reset input fields and result
def reset_fields():
    entry_weight.delete(0, tk.END)
    entry_height.delete(0, tk.END)
    result_label.config(text="", bg=bg_color)

# Colors
bg_color = "lightblue"
accent_color = "#4CAF50"
text_color = "#333"

# GUI Window
root = tk.Tk()
root.title("BMI Checker")
root.geometry("350x350")
root.resizable(False, False)
root.configure(bg=bg_color)

# Title
title_label = tk.Label(root, text="BMI Checker", font=("Arial", 18, "bold"), bg=bg_color, fg=accent_color)
title_label.pack(pady=15)

# Weight input
tk.Label(root, text="Weight (kg):", bg=bg_color, fg=text_color).pack()
entry_weight = tk.Entry(root, font=("Arial", 12))
entry_weight.pack(pady=5)

# Height input
tk.Label(root, text="Height (cm):", bg=bg_color, fg=text_color).pack()
entry_height = tk.Entry(root, font=("Arial", 12))
entry_height.pack(pady=5)

# Buttons
btn_frame = tk.Frame(root, bg=bg_color)
btn_frame.pack(pady=20)

calc_button = tk.Button(btn_frame, text="Calculate", command=calculate_bmi, bg=accent_color, fg="white", width=10)
calc_button.grid(row=0, column=0, padx=10)

reset_button = tk.Button(btn_frame, text="Reset", command=reset_fields, bg="#f44336", fg="white", width=10)
reset_button.grid(row=0, column=1, padx=10)

# Result display
result_label = tk.Label(root, text="", font=("Arial", 14), bg=bg_color, fg="black", wraplength=250, justify="center")
result_label.pack(pady=15)

# Run the app
root.mainloop()
