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

Configuration

!!!Ensure that you have set the OpenAI API key in your environment variables for the application to function correctly.!!!

# Contributing
Contributions to AI-Snapshot-Analysis are welcome. Please fork the repository and submit a pull request with your proposed changes.


AI-Snapshot-Analysis is released under MIT, which permits use, modification, and distribution.
