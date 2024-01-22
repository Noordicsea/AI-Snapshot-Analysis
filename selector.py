# selector.py
import tkinter as tk
from tkinter import Canvas
from PIL import ImageTk, ImageGrab
import pytesseract
import os
import tempfile
from PIL import Image

def process_selection(image, coords):
    try:
        x0, y0, x1, y1 = coords['start'] + coords['end']
        x0, x1 = sorted([x0, x1])
        y0, y1 = sorted([y0, y1])
        cropped_image = image.crop((x0, y0, x1, y1))
        text = pytesseract.image_to_string(cropped_image)
        return text
    except Exception as e:
        print(f"Error during text extraction: {e}")
        return ""

def process_screenshot(screenshot):
    root = tk.Tk()
    root.title("Select Area")
    root.attributes('-fullscreen', True)
    canvas = Canvas(root, width=screenshot.width, height=screenshot.height)
    canvas.pack(fill="both", expand=True)

    def exit_screenshot():
        root.quit()

    def on_escape(event):
        exit_screenshot()

    coords, tk_screenshot, esc_pressed = select_area(root, canvas, screenshot, exit_screenshot)

    # Exit and destroy the root window
    root.quit()
    root.destroy()

    if esc_pressed:
        return None, None, None

    extracted_text = process_selection(screenshot, coords)
    return coords, tk_screenshot, extracted_text

def select_area(root, canvas, screenshot, exit_function):
    coords = {'start': (0, 0), 'end': (0, 0)}
    rect = None
    esc_pressed = [False]

    tk_screenshot = ImageTk.PhotoImage(master=canvas, image=screenshot)
    canvas.create_image(0, 0, image=tk_screenshot, anchor="nw")

    def on_click(event):
        coords['start'] = (event.x, event.y)

    def on_drag(event):
        nonlocal rect
        coords['end'] = (event.x, event.y)
        if rect:
            canvas.delete(rect)
        rect = canvas.create_rectangle(*coords['start'], *coords['end'], outline='red')

    def on_release(event):
        coords['end'] = (event.x, event.y)
        exit_function()

    # Define the on_escape function before binding it
    def on_escape(event):
        nonlocal esc_pressed
        esc_pressed[0] = True
        root.quit()  # Directly quit the main loop

    canvas.bind("<ButtonPress-1>", on_click)
    canvas.bind("<B1-Motion>", on_drag)
    canvas.bind("<ButtonRelease-1>", on_release)
    root.bind("<Escape>", on_escape)
    root.protocol("WM_DELETE_WINDOW", exit_function)

    root.mainloop()
    return coords, tk_screenshot, esc_pressed[0]
