import tkinter as tk

# ---------------- THEME ----------------
dark_mode = False

def apply_theme():
    bg = "#1e1e1e" if dark_mode else "#ffffff"
    fg = "#ffffff" if dark_mode else "#000000"
    btn_bg = "#333333" if dark_mode else "#f0f0f0"
    entry_bg = "#2b2b2b" if dark_mode else "#ffffff"

    root.configure(bg=bg)
    entry.configure(bg=entry_bg, fg=fg, insertbackground=fg)

    for btn in buttons_list:
        btn.configure(bg=btn_bg, fg=fg)

# ---------------- FUNCTIONS ----------------
history = []

def click(event):
    entry.insert(tk.END, event.widget.cget("text"))

def clear():
    entry.delete(0, tk.END)

def backspace():
    entry.delete(len(entry.get())-1, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        history.append(f"{entry.get()} = {result}")
        update_history()

        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def update_history():
    history_box.delete(0, tk.END)
    for item in history[-5:]:
        history_box.insert(tk.END, item)

def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    apply_theme()

def key_input(event):
    entry.insert(tk.END, event.char)

# ---------------- UI ----------------
root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("450x700")

entry = tk.Entry(root, font=("Arial", 20), justify="right")
entry.pack(fill="both", padx=10, pady=10)

# History box
history_box = tk.Listbox(root, height=5)
history_box.pack(fill="both", padx=10)

# Buttons frame
buttons_frame = tk.Frame(root)
buttons_frame.pack(expand=True, fill="both")

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

buttons_list = []

for row in buttons:
    frame = tk.Frame(buttons_frame)
    frame.pack(expand=True, fill="both")

    for btn in row:
        b = tk.Button(frame, text=btn, font=("Arial", 15))
        b.pack(side="left", expand=True, fill="both", padx=3, pady=3)
        buttons_list.append(b)

        if btn == "=":
            b.bind("<Button-1>", lambda e: calculate())
        else:
            b.bind("<Button-1>", click)

# Extra buttons
extra_frame = tk.Frame(root)
extra_frame.pack(fill="both")

tk.Button(extra_frame, text="⌫ Backspace", command=backspace).pack(side="left", expand=True, fill="both")
tk.Button(extra_frame, text="Clear", command=clear).pack(side="left", expand=True, fill="both")
tk.Button(extra_frame, text="🌙 Theme", command=toggle_theme).pack(side="left", expand=True, fill="both")

# Keyboard support
root.bind("<Key>", key_input)

apply_theme()
root.mainloop()