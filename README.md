# Data Cleanup Tool

## Overview

The **Data Cleanup Tool** is a Python script that is particularly useful for users who work with large, messy datasets and need a quick way to standardize and clean their data.

## Features

- Remove duplicate rows from a CSV file (optional).
- Clean specific columns using a customizable regular expression.
- Process and save cleaned data to a new file.
- Provides user-friendly feedback and error handling.

## Usage
### Command-line Options

```
usage: data_cleanup_tool.py [-h] [-c COLUMN] [-d] input_file output_file
```

### positional arguments:
- `input_file`: Path to the input CSV file. 
- `output_file`: Path to save the cleaned CSV file.

### optional arguments:
- `-c COLUMN, --column COLUMN:` The name of the column to clean using a regular expression.
- `-d, --deduplicate:` Remove duplicate rows from the CSV.
- `-h, --help:` Show this help message and exit.

