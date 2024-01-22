# AI-Snapshot-Analysis
AI-Snapshot-Analysis is a Python application designed to integrate advanced image and text analysis capabilities with a user-friendly interface. Leveraging OpenAI's powerful models, this tool enables users to capture and analyze specific areas of their screen, providing insightful feedback based on artificial intelligence.
Features

    Screenshot Selection: Users can capture and select specific areas of their screen for analysis.
    Image and Text Processing: Processes images and text extracted from screenshots using OpenAI's models.
    Interactive GUI: A Tkinter-based GUI allowing intuitive interaction and ease of use.
    Prompt Book: A feature to save and reuse custom prompts for analysis.
    Clipboard Integration: Users can copy the analysis results directly to the clipboard.

Components

The application is composed of several Python scripts, each handling a different aspect of the functionality:

    GUI.py: The main graphical user interface.
    main.py: Entry point of the application.
    openai_model.py: Handles communication with OpenAI's API for image and text processing.
    photo_handler.py: Manages the image capture and processing workflow.
    prompt_book.py: Manages the saved prompts for repeated use.
    selector.py: Facilitates selection of screen area for analysis.
    text_handler.py: Handles the text extraction and processing from screenshots.

Installation and Usage

To use AI-Snapshot-Analysis, you'll need Python installed on your system. Follow these steps:

    Clone or download the repository.
    Install the required dependencies (listed in a separate requirements.txt file).
    Set your OpenAI API key as an environment variable.
    Run main.py to start the application.

Dependencies

    Tkinter
    OpenAI
    PIL (Python Imaging Library)
    Pytesseract
    Requests

# Configuration
Ensure that you have set the OpenAI API key in your environment variables for the application to function correctly!
Make sure to add pytesseract to your Systems environment variables!


# Contributing
Contributions to AI-Snapshot-Analysis are welcome. Please fork the repository and submit a pull request with your proposed changes.



# AI-Snapshot-Analysis Setup Guide

## Step 1: Install Python
1. **Download Python**: Go to the [official Python website](https://www.python.org/downloads/) and download the latest version of Python for Windows.
2. **Install Python**: 
    - Run the downloaded file.
    - During installation, make sure to check the box that says **"Add Python to PATH"**. This is crucial for running Python from the Command Prompt.
    - Follow the installation instructions and finish the setup.

## Step 2: Install Pytesseract
1. **Download Pytesseract**: Visit the [Pytesseract GitHub page](https://github.com/UB-Mannheim/tesseract/wiki) and download the installer for Windows.
2. **Install Pytesseract**: 
    - Run the downloaded installer.
    - Follow the installation instructions. Note the installation path as you will need it to set the PATH variable.
3. **Add Pytesseract to PATH**:
    - After installation, add Pytesseract to the system PATH.
    - Right-click on 'This PC' or 'Computer' on the desktop, then select 'Properties'.
    - Click on 'Advanced system settings' and then 'Environment Variables'.
    - In the 'System variables' section, find and select the 'Path' variable, then click 'Edit'.
    - Click 'New' and add the path to the Pytesseract installation (e.g., `C:\Program Files\Tesseract-OCR`).
    - Click OK to close all dialogs.

## Step 3: Set Up the Project
1. **Download AI-Snapshot-Analysis**: Download the source code for the AI-Snapshot-Analysis tool. If it's on a platform like GitHub, there should be an option to download it as a ZIP file.
2. **Extract Files**: Once downloaded, right-click on the ZIP file and choose "Extract All" to extract the files to a folder.

## Step 4: Open Command Prompt
1. **Search for Command Prompt**: Click on the Windows Start menu and type `cmd`. You'll see 'Command Prompt' - click on it to open.
   
## Step 5: Install Dependencies
1. **Navigate to Project Folder**:
    - In the Command Prompt, use the `cd` command to change directories to the folder where the AI-Snapshot-Analysis code is located.
    - For example, if the folder is on the desktop, the command might be something like `cd Desktop\AI-Snapshot-Analysis`.
2. **Install Requirements**:
    - Ensure that a file named `requirements.txt` is in the project folder.
    - In the Command Prompt, type `pip install -r requirements.txt` and press Enter. This will install all the necessary Python libraries.

## Step 6: Set Up OpenAI API Key
1. **Get OpenAI API Key**: You need an API key from OpenAI. If you don't have one, you'll need to sign up at [OpenAI's website](https://openai.com/) and obtain an API key.
2. **Set Environment Variable for API Key**:
    - Right-click on 'This PC' or 'Computer' on the desktop or in File Explorer, and select 'Properties'.
    - Click on 'Advanced system settings' and then on 'Environment Variables'.
    - Under 'User variables', click 'New...' and add a new variable.
        - Variable name: `OPENAI_API_KEY`
        - Variable value: [Your OpenAI API Key]
    - Click OK and close all the windows.

## Step 7: Run the Application
1. **Run the Application**:
    - Go back to the Command Prompt (make sure you're in the AI-Snapshot-Analysis project directory).
    - Type `python main.py` and press Enter to run the application.

## Step 8: Using the Application
- The AI-Snapshot-Analysis GUI should now be open. You can use the tool to capture and analyze screenshots as per the tool's features.

## Additional Notes
- If you encounter any errors related to missing packages or other issues, you might need to revisit the installation steps or check if the `requirements.txt` file includes all necessary packages.
- It's important to restart the Command Prompt after setting environment variables to ensure they are loaded correctly.

