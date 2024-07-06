# Zip Processor

A Python application that processes ZIP files to update the `pack_format` number in `.mcmeta` files using a GUI built with Tkinter. This application is designed to work cross-platform on Windows, macOS, and Linux.

## Features

- Select input and output directories through a graphical interface.
- Specify a new `pack_format` number to update in `.mcmeta` files.
- Processes all ZIP files in the input directory and creates modified copies in the output directory.

## Requirements

- Python 3.6 or higher
- Tkinter (usually included with Python)
- PyInstaller (for creating executables)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/zip-processor.git
    cd zip-processor
    ```

2. **Set up a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the application:**

    ```bash
    python src/main.py
    ```

2. **Using the GUI:**

    - Click "Browse" to select the input folder containing ZIP files.
    - Click "Browse" to select the output folder where modified ZIP files will be saved.
    - Enter the new `pack_format` number.
    - Click "Start Processing" to begin the update process.

## Creating Executables

### Windows

1. **Install PyInstaller:**

    ```bash
    pip install pyinstaller
    ```

2. **Create the executable:**

    ```bash
    pyinstaller --onefile --windowed --distpath ./dist --workpath ./build src/main.py
    ```
3. ** Use the executable in the dist folder: dist/main.exe **
    ```
        main.exe
   ```
### macOS/Linux

1. **Install PyInstaller:**

    ```bash
    pip install pyinstaller
    ```

2. **Create the executable:**

    ```bash
    pyinstaller --onefile --windowed --distpath ./dist --workpath ./build src/main.py
    ```
3. **Use the executable in the dist folder : dist/main.sh**
    ```
        ./main.sh 
   ```


## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

