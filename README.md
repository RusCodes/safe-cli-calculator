# Safe CLI Calculator

A simple command-line calculator written in Python. This project demonstrates how to safely evaluate mathematical expressions 
from user input without using the dangerous `eval()` function, which can lead to security vulnerabilities.

## Features

* **Safe Evaluation**: Parses expressions using the `ast` (Abstract Syntax Tree) module to ensure only numeric and supported 
mathematical operations are executed.
* **CLI Mode**: Evaluate a single expression directly from the command line.
* **REPL Mode**: An interactive Read-Eval-Print Loop for continuous calculations.

## How to Run

1.  Make sure you have Python installed.
2.  Save the code in a file named `safe_eval.py`.
3.  Run from the terminal:

### CLI Mode

```bash
python safe_eval.py "2 + 3 * 4"
