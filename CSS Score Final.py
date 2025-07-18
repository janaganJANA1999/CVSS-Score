import tkinter as tk
from tkinter import ttk, messagebox
from cvss import CVSS3

# CVSS Metric Options
options = {
    "AV": {"name": "Attack Vector", "choices": {"N": "Network", "A": "Adjacent", "L": "Local", "P": "Physical"}},
    "AC": {"name": "Attack Complexity", "choices": {"L": "Low", "H": "High"}},
    "PR": {"name": "Privileges Required", "choices": {"N": "None", "L": "Low", "H": "High"}},
    "UI": {"name": "User Interaction", "choices": {"N": "None", "R": "Required"}},
    "S": {"name": "Scope", "choices": {"U": "Unchanged", "C": "Changed"}},
    "C": {"name": "Confidentiality", "choices": {"N": "None", "L": "Low", "H": "High"}},
    "I": {"name": "Integrity", "choices": {"N": "None", "L": "Low", "H": "High"}},
    "A": {"name": "Availability", "choices": {"N": "None", "L": "Low", "H": "High"}}
}

# Create window
root = tk.Tk()
root.title("CVSS v3.1 Score Generator")
root.geometry("520x680")
root.resizable(False, False)

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

tk.Label(frame, text="CVSS v3.1 Calculator", font=("Arial", 18, "bold")).pack(pady=10)

# Store dropdown selections
selections = {}

# Create dropdowns
for metric in options:
    full_name = options[metric]["name"]
    choices = options[metric]["choices"]

    label = tk.Label(frame, text=f"{full_name} ({metric}):", font=("Arial", 11))
    label.pack(anchor='w', pady=(10, 0))

    var = tk.StringVar()
    combo = ttk.Combobox(frame, textvariable=var, state="readonly", width=42)
    combo['values'] = [f"{code} = {desc}" for code, desc in choices.items()]
    combo.pack()
    selections[metric] = var

# Vector & Score Output
vector_label = tk.Label(frame, text="\nVector will appear here", wraplength=460, justify="left", font=("Courier", 10))
vector_label.pack(pady=(20, 5))

score_label = tk.Label(frame, text="", font=("Arial", 14, "bold"))
score_label.pack()

# Calculation Logic
def calculate_cvss():
    try:
        vector_parts = ["CVSS:3.1"]
        for metric in options:
            selected = selections[metric].get()
            if not selected:
                raise ValueError(f"{options[metric]['name']} ({metric}) is not selected.")
            code = selected.split(" = ")[0].strip()
            vector_parts.append(f"{metric}:{code}")

        vector_string = "/".join(vector_parts)
        cvss_obj = CVSS3(vector_string)
        base_score = cvss_obj.scores()[0]

        vector_label.config(text=f"📋 Vector: {vector_string}")
        score_label.config(text=f"🔥 Base Score: {base_score}", fg="green")

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n\n{str(e)}")

# Styled Button
button_frame = tk.Frame(frame)
button_frame.pack(pady=20)

btn = tk.Button(button_frame,
                text="🔍 Generate CVSS v3.1 Score",
                command=calculate_cvss,
                bg="#1E90FF", fg="white",
                font=("Arial", 12, "bold"),
                relief="raised", bd=3,
                padx=20, pady=10)
btn.pack()

# Start GUI
root.mainloop()
