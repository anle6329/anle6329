from AppOpener import open ,close
import os 
import shutil
import pathlib
def open_application(arguments_str):
    try:
        open(arguments_str, output=False , throw_error=True)
    except ValueError(f"Failed to open app") as e :
        print(e)
        raise
    return f"Application '{arguments_str}' opened successfully."
def close_application(arguments_str):
    try:
        close(arguments_str, output=False , throw_error=True)
    except ValueError(f"Failed to close app") as e:
        print(e)
        raise
    return f"Application '{arguments_str}' closed successfully."
def special_command(arguments_str):
    # THIS IS A PLACEHOLDER FUNCTION TO CALL THE AGENT FOR SPECIAL COMMANDS.
    return f"Special command executed with arguments: {arguments_str}"
def get_status(arguments_str):
    
    return f"Status of '{arguments_str}': Running"
