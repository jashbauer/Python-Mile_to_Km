import tkinter as tk

# VARIABLES DEFINITIONS
FONT = ("arial", 20, "bold")

# WINDOW SETUP
root = tk.Tk()
root.minsize(width=600, height=200)
root.title("Miles to Kilometers Converter")
root.config(padx=10, pady=10)

# INSTRUCTION LABEL
instr_label = tk.Label(text="Enter Miles:", font=FONT)
instr_label.grid(row=0, column=0)

# ENTRY BOX
miles_box = tk.Entry(width=10)
miles_box.grid(row=0, column=1, padx=10)

# KM OUTPUT
km_label_flag = tk.Label(text="Converts to: ", font=FONT)
km_label_flag.grid(row=1, column=0, padx=10)

km_label = tk.Label(text="0", font=FONT)
km_label.grid(row=1, column=1, padx=10)

# CONVERTER FUNCTION


def converter():
    val = miles_box.get()
    val_list = []
    if "," in val:
        for char in val:
            val_list.append(char)
        for i in range(len(val_list) - 1):
            if val_list[i] == ",":
                val_list[i] = "."
        val = "".join(map(str, val_list))
    val = float(val)
    val_km = val*1.609
    km_label.config(text=f"{val_km:.2f} Km.")


# BUTTON AND ACTION
conv_button = tk.Button(text="Click to convert.", command=converter)
conv_button.grid(row=0, column=3, padx=10)

root.mainloop()
