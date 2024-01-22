from PIL import ImageGrab
import tkinter as tk
from selector import process_screenshot
from openai_model import process_text_with_prompt

def handle_text(prompt, text_widget):
    # Grab a screenshot of the entire screen
    screenshot = ImageGrab.grab()

    # Process the screenshot to select an area and extract text from it
    coords, _, extracted_text = process_screenshot(screenshot)

    # If text is extracted from the screenshot, process it with the given prompt
    if extracted_text:
        # Combine the extracted text with the user's prompt and send it to the OpenAI model
        response = process_text_with_prompt(extracted_text, prompt)
    else:
        # If no text is found in the selected area, set an appropriate response
        response = "No text was found in the selected area."

    # Update the Text widget in the GUI with the response
    text_widget.config(state=tk.NORMAL)  # Enable editing of the widget
    text_widget.delete(1.0, tk.END)      # Clear existing text in the widget
    text_widget.insert(tk.END, response) # Insert the new response into the widget
    text_widget.config(state=tk.DISABLED) # Disable editing of the widget after updating it
