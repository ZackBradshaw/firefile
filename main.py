import os
import logging
import argparse
import subprocess
from interpreter import interpreter

def suggest_mojo_improvements(mojo_code):
    """
    Uses Open Interpreter to suggest improvements for Mojo code.
    
    Args:
    - mojo_code (str): The Mojo code to be improved.
    
    Returns:
    - str: The improved Mojo code.
    """
    try:
        # Initialize Open Interpreter chat session
        response = interpreter.chat(f"Suggest improvements for this Mojo code: {mojo_code}")
        improved_mojo_code = response if response else mojo_code
        return improved_mojo_code
    except Exception as e:
        print(f"Failed to suggest improvements for Mojo code. Error: {e}")
        return mojo_code

def convert_python_file_to_mojo_file(python_file_path):
    """
    Changes the file extension of a given Python file to .🔥, indicating it is now a Mojo file.
    This function assumes Mojo is a superset of Python, thus no syntax changes are needed.
    However, it also interacts with Open Interpreter to suggest improvements for the Mojo code.
    
    Args:
    - python_file_path (str): The file path of the Python file to be converted.
    
    Returns:
    - str: The file path of the converted Mojo file.
    """
    # Change the file extension from .py to .🔥
    mojo_file_path = python_file_path.rsplit('.', 1)[0] + '.🔥'
    
    try:
        with open(python_file_path, 'r') as python_file:
            python_code = python_file.read()
        
        # Although Mojo is a superset of Python, we still check for improvements
        mojo_code = suggest_mojo_improvements(python_code)
        
        with open(mojo_file_path, 'w') as mojo_file:
            mojo_file.write(mojo_code)
        
        print(f"Converted {python_file_path} to {mojo_file_path} with potential improvements suggested.")
    except Exception as e:
        print(f"Failed to convert {python_file_path}. Error: {e}")
    
    return mojo_file_path

def convert_directory_py_to_mojo(directory_path):
    """
    Converts all Python files in a directory to Mojo files and suggests improvements using Open Interpreter.
    
    Args:
    - directory_path (str): The path to the directory containing Python files.
    """
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".py"):
                python_file_path = os.path.join(root, file)
                convert_python_file_to_mojo_file(python_file_path)

def main():
    """
    Main function to handle command line arguments for converting Python files to Mojo format.
    Now prompts the user for the directory path if not provided as an argument.
    """
    parser = argparse.ArgumentParser(description="Convert Python files to Mojo format using Open Interpreter for improvements.")
    parser.add_argument("-d", "--directory_path", type=str, help="The directory path containing Python files to convert.", required=False)
    args = parser.parse_args()

    if not args.directory_path:
        directory_path = input("Please enter the directory path containing Python files to convert: ")
    else:
        directory_path = args.directory_path

    logging.basicConfig(level=logging.INFO)
    convert_directory_py_to_mojo(directory_path)

if __name__ == "__main__":
    main()

