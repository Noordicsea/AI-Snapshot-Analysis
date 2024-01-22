import tkinter as tk
from tkinter import Listbox, Toplevel
import json
import os

class PromptBook:
    def __init__(self, parent, callback):
        self.parent = parent
        self.callback = callback
        self.prompts = self.load_prompts()

    def load_prompts(self):
        if not os.path.exists("prompts.json"):
            # If the file doesn't exist, create an empty JSON file
            with open("prompts.json", "w") as file:
                json.dump({}, file)
            print("Created an empty prompts.json file.")
            return {}

        # If the file exists, load its contents
        with open("prompts.json", "r") as file:
            prompts = json.load(file)
            print("Loaded prompts:", prompts)  # Debug print
            return prompts

    def open_prompt_book(self):
        window = Toplevel(self.parent)
        window.title("Prompt Book")
        listbox = Listbox(window)
        listbox.pack(fill="both", expand=True)

        for label in self.prompts:
            print("Adding label to listbox:", label)  # Debug print
            listbox.insert(tk.END, label)

        def on_select(event):
            w = event.widget
            index = int(w.curselection()[0])
            value = w.get(index)
            self.callback(self.prompts[value])
            window.destroy()

        listbox.bind('<<ListboxSelect>>', on_select)

    def save_prompt(self, label, prompt):
        self.prompts[label] = prompt
        self.save_prompts()

    def save_prompts(self):
        with open("prompts.json", "w") as file:
            json.dump(self.prompts, file)