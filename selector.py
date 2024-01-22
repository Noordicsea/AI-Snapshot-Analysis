mport tkinter as tk
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

def select_area(root, canvas, screenshot):
    coords = {'start': (0, 0), 'end': (0, 0)}
    rect = None

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
        root.quit()

    canvas.bind("<ButtonPress-1>", on_click)
    canvas.bind("<B1-Motion>", on_drag)
    canvas.bind("<ButtonRelease-1>", on_release)

    root.mainloop()
    return coords, tk_screenshot

def process_screenshot(screenshot):
    root = tk.Tk()
    root.title("Select Area")
    root.attributes('-fullscreen', True)
    canvas = Canvas(root, width=screenshot.width, height=screenshot.height)
    canvas.pack(fill="both", expand=True)
    coords, tk_screenshot = select_area(root, canvas, screenshot)
    root.destroy()
    extracted_text = process_selection(screenshot, coords)
    return coords, tk_screenshot, extracted_text
