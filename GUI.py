import tkinter as tk
from tkinter import simpledialog
from prompt_book import PromptBook  # Import the PromptBook class

# Handlers for the simplified functionality
import photo_handler
import text_handler

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Interactive Screenshot Tool")
        self.initialize_window_size()
        self.prompt_book = PromptBook(self, self.set_prompt)  # Initialize prompt_book
        self.create_widgets()  # Then call create_widgets

    def set_prompt(self, prompt):
        self.input_prompt.delete(0, tk.END)
        self.input_prompt.insert(0, prompt)

    def initialize_window_size(self):
        screen_width = self.winfo_screenwidth() // 3
        screen_height = 530
        self.geometry(f"{screen_width}x{screen_height}")

    def create_widgets(self):
        self.configure(bg='#04151F')  # Rich black for main background
        button_font = ('Roboto', 12)
        button_bg = '#183A37'  # Dark slate gray for button background
        button_fg = '#EFD6AC'  # Wheat for button foreground text
        button_active_bg = '#C44900'  # Mahogany for button active background
        button_active_fg = '#EFD6AC'  # Wheat for button active foreground text
        label_font = ('Roboto', 20, 'bold')
        text_bg = '#432534'  # Dark purple for text background
        text_fg = '#EFD6AC'  # Wheat for text foreground

        # Title Label
        self.title_label = tk.Label(self, text="Interactive Screenshot Tool", bg='#04151F', fg='#EFD6AC', font=label_font)
        self.title_label.pack(pady=10)

        # Label for the Input Prompt
        self.input_prompt_label = tk.Label(self, text="Message regarding selection:", bg='#04151F', fg='#EFD6AC', font=('Roboto', 10))
        self.input_prompt_label.pack(padx=20, pady=(5, 0))

        # Input Prompt Text Entry
        self.input_prompt = tk.Entry(self, font=('Roboto', 12), bg=text_bg, fg=text_fg)
        self.input_prompt.pack(fill='x', padx=20, pady=5)

        # Save Prompt Button
        self.save_prompt_button = tk.Button(self, text="Save Prompt", 
                                            command=self.save_prompt,
                                            font=button_font, bg=button_bg, fg=button_fg)
        self.save_prompt_button.pack(padx=20, pady=5)

        # Buttons
        self.photo_button = tk.Button(self, text="Examine Photo", 
                                    command=lambda: photo_handler.handle_photo(self.input_prompt.get(), self.response_text),
                                    font=button_font, bg=button_bg, fg=button_fg,
                                    activebackground=button_active_bg, activeforeground=button_active_fg)
        self.photo_button.pack(fill='x', padx=20, pady=5)

        self.text_button = tk.Button(self, text="Examine Text", 
                                    command=lambda: text_handler.handle_text(self.input_prompt.get(), self.response_text),
                                    font=button_font, bg=button_bg, fg=button_fg,
                                    activebackground=button_active_bg, activeforeground=button_active_fg)
        self.text_button.pack(fill='x', padx=20, pady=5)

        # Response Text Widget
        self.response_text = tk.Text(self, height=10, width=50, bg=text_bg, fg=text_fg)
        self.response_text.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10, expand=True)

        # Copy to Clipboard Button
        self.copy_button = tk.Button(self, text="Copy to Clipboard", command=self.copy_to_clipboard,
                                    font=button_font, bg=button_bg, fg=button_fg,
                                    activebackground=button_active_bg, activeforeground=button_active_fg)
        self.copy_button.pack(side=tk.TOP, pady=5, expand=True)

        # Prompt Book Button
        self.prompt_book_button = tk.Button(self, text="Prompt Book", 
                                            command=self.prompt_book.open_prompt_book,
                                            font=button_font, bg=button_bg, fg=button_fg,
                                            activebackground=button_active_bg, activeforeground=button_active_fg)
        self.prompt_book_button.pack(side=tk.TOP, pady=5, expand=True)

        # Update each widget to apply rounded corners and new styling
        self.style_widgets()



    def style_widgets(self):
        # Function to style buttons and text entry
        widgets = [self.save_prompt_button, self.photo_button, self.text_button, 
                self.prompt_book_button, self.copy_button, self.input_prompt]

        for widget in widgets:
            if isinstance(widget, tk.Button):
                widget.config(
                    font=('Roboto', 12),
                    bg='#183A37', fg='#EFD6AC',
                    activebackground='#C44900', activeforeground='#EFD6AC',
                    relief='flat'
                )
            elif isinstance(widget, tk.Entry):
                widget.config(
                    font=('Roboto', 12),
                    fg='#EFD6AC', insertbackground='#EFD6AC',
                    bg='#432534', relief='solid', highlightthickness=1, highlightbackground="#432534"
                )

    def save_prompt(self):
        prompt_label = simpledialog.askstring("Save Prompt", "Enter a label for this prompt:")
        if prompt_label:
            self.prompt_book.save_prompt(prompt_label, self.input_prompt.get())

    def copy_to_clipboard(self):
        text = self.response_text.get("1.0", tk.END).strip()
        self.clipboard_clear()
        self.clipboard_append(text)

    def exit_application(self):
        self.destroy()

if __name__ == "__main__":
    app = GUI()
    app.mainloop()
