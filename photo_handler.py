import io
import base64
from PIL import ImageGrab
import tkinter as tk
from selector import process_screenshot
from openai_model import process_image_with_prompt

def handle_photo(prompt, text_widget):
    # Capture a screenshot
    screenshot = ImageGrab.grab()
    coords, _, _ = process_screenshot(screenshot)

    # Check if an area was selected and process it
    if coords:
        # Crop the image based on the selected coordinates
        cropped_image = crop_image(screenshot, coords)
        # Convert the cropped image to base64 encoding
        base64_image = encode_to_base64(cropped_image)
        # Send the base64 image and prompt to OpenAI for processing
        response = process_image_with_prompt(base64_image, prompt)
    else:
        # If no area was selected, set an appropriate response
        response = "No area was selected."
    
    # Update the Text widget with the response
    text_widget.config(state=tk.NORMAL)
    text_widget.delete(1.0, tk.END)
    text_widget.insert(tk.END, response)
    text_widget.config(state=tk.DISABLED)

def crop_image(image, coords):
    # Get coordinates for cropping
    x0, y0, x1, y1 = coords['start'] + coords['end']
    # Ensure coordinates are in the correct order
    x0, x1 = sorted([x0, x1])
    y0, y1 = sorted([y0, y1])
    # Crop the image using PIL's crop function
    return image.crop((x0, y0, x1, y1))

def encode_to_base64(image):
    # Create an in-memory buffer
    buffer = io.BytesIO()
    # Save the image to the buffer in PNG format
    image.save(buffer, format="PNG")
    # Encode the buffer's contents in base64 and return
    return base64.b64encode(buffer.getvalue()).decode('utf-8')
