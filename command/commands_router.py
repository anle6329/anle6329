from config.tool_list import command_types , commands
from action_tools.tool_registry import execute_tool
import command.commands 
def identify_command_type(transcript):
    if transcript is None:
            return None
    words = transcript.lower().split() 
    for command in command_types:
        keywords = command_types[command]
        if(any(keyword in words for keyword in keywords)):
            return command
    return None
def extract_arguments(transcript, command_type):
    if transcript is None or command_type is None:
        return None
    if command_type not in command_types:
        raise ValueError(f"Command type '{command_type}' is not recognized.")
    words = transcript.lower().split()
    for keyword in command_types[command_type]:
        if keyword in words:
            pos = words.index(keyword)
            break
    else :
        raise ValueError(f"No keyword found for command type '{command_type}' in transcript.")
    arguments = words[pos + 1:]
    if not arguments:
        raise ValueError(f"Please provide specifc arguments for the command '{command_type}'.")
    return arguments
    
def command_router(transcript) :
    command_type = identify_command_type(transcript)
    if command_type is None:
            raise ValueError("No valid command found.")
    command = commands.get(command_type)
    arguments = extract_arguments(transcript, command_type)
    arguments_str = " ".join(arguments)
    return execute_tool(command, arguments_str)
        
    
    
    
    
