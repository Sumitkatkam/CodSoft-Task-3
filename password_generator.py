import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        # Frames
        self.frame_input = tk.Frame(root)
        self.frame_input.pack(pady=10)

        self.frame_buttons = tk.Frame(root)
        self.frame_buttons.pack(pady=10)

        self.frame_display = tk.Frame(root)
        self.frame_display.pack(pady=10)

        # Input Field
        self.label_length = tk.Label(self.frame_input, text="Password Length:")
        self.label_length.pack(side=tk.LEFT, padx=5)

        self.entry_length = tk.Entry(self.frame_input, width=10)
        self.entry_length.pack(side=tk.LEFT, padx=5)

        # Buttons
        self.btn_generate = tk.Button(self.frame_buttons, text="Generate Password", command=self.generate_password)
        self.btn_generate.pack(side=tk.LEFT, padx=5)

        self.btn_copy = tk.Button(self.frame_buttons, text="Copy to Clipboard", command=self.copy_password)
        self.btn_copy.pack(side=tk.LEFT, padx=5)

        # Display Area
        self.display_text = tk.Entry(self.frame_display, width=50, state='readonly')
        self.display_text.pack()

    def generate_password(self):
        length = self.entry_length.get()
        if not length.isdigit() or int(length) <= 0:
            messagebox.showerror("Error", "Please enter a valid positive number for length.")
            return

        length = int(length)
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))

        self.display_text.config(state='normal')
        self.display_text.delete(0, tk.END)
        self.display_text.insert(0, password)
        self.display_text.config(state='readonly')

    def copy_password(self):
        password = self.display_text.get()
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            messagebox.showinfo("Info", "Password copied to clipboard!")
        else:
            messagebox.showerror("Error", "No password to copy!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
