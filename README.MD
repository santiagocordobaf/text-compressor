Project developed by Santiago Cordoba Fuentes.

# Text compressor and decompressor.

Data compression is the reduction of the volume of data that can be processed to represent a certain information using a smaller amount of space. In this project, the use of RLE compression or Run-length encoding is a very simple form of data compression in which data sequences with the same consecutive value are stored as a single value plus its count.

## Prerequisites

- Python 3.x installed on your machine.
- Git installed to clone the repository.

## Project Architecture

In this project the library used for the validation of unit tests is **unittest** which provides us with a set of tools to build and execute tests.

## Files description 

This project is structured as follows:

```
text-compressor/
├── .vscode
│   └── settings.json
│
│
├── src
│   ├── console
│   │    └── rle_compression_console.py # Logic for the command line interface
│   │    
│   ├── functionalities
│   |   ├── _init_.py
│   |   └── rle_compression.py          # Logic of the functionalities for text compression and decompression 
│   │    
│   └── gui
|       ├── _init_.py
│       └── rle_compression_gui.py      # Logic of text compression and decompression functionalities implemented in kivy 
│
├── tests
│   ├── _init_.py
│   └── rle_compression_tests.py        # Tests for text compression/decompression logic
│ 
│
├── .gitignore    # Paths excluded from version control
├── LICENSE       # Project license
└── README.md     # Project documentation
```

## Installation and Usage

Open your terminal (PowerShell, Command Prompt, or any terminal you prefer).
1. Navigate to the folder where you want to clone the project, using the `cd` command.
2. Run the following command to clone the repository: 
    > $> git clone https://github.com/santiagocordobaf/text-compressor.git
3. Navigate to the project folder:
    > $> cd text-compressor

### Running Unit Test

4. To run the unit tests performed, use the following command:
    > $> python -m unittest discover -s tests -p "*.py"
- This will discover and run all the test cases within the tests folder.

### Running the Program
5. To run the console or kivy interface of the program in which you can compress and decompress texts, use the following commands:
    > $> python src/console/rle_compression_console.py


    > $> python src/gui/rle_compression_console_gui.py

This is a second part of the release for this project after doing some refactoring and applying clean code principles.
