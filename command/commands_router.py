from config.tool_list import command_types , commands
from action_tools.tool_registry import execute_tool 
def identify_command_type(words):
    if words is None:
            return None
    for command in command_types:
        keywords = command_types[command]
        if(any(keyword in words for keyword in keywords)):
            return command
    return None
def extract_arguments(words, command_type):
    if words is None or command_type is None:
        return None
    if command_type not in command_types:
        raise ValueError(f"Command type '{command_type}' is not recognized.")
    for keyword in command_types[command_type]:
        if keyword in words:
            pos = words.index(keyword)
            break
    else :
        raise ValueError(f"No keyword found for command type '{command_type}' in transcript.")
    arguments = words[pos + 1:]
    if not arguments:
        raise ValueError(f"Please provide arguments for the command '{command_type}'.")
    return arguments
    
def command_router(transcript) :
    if not isinstance(transcript, str) or not transcript.strip():
        return None
    words = transcript.lower().split()
    clean_words = [word.strip("!?,.:;") for word in words]
    command_type = identify_command_type(clean_words)
    if command_type is None:
            raise ValueError("No valid command type found.")
    command = commands.get(command_type)
    if command is None:
        raise ValueError(f"Command '{command_type}' is not recognized.")
    arguments = extract_arguments(clean_words, command_type)
    arguments_str = " ".join(arguments)
    return execute_tool(command, arguments_str)
        
    
    
    
    
