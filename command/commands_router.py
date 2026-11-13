from config.tool_list import command_types , connecter_list
from action_tools.tool_registry import execute_tool 
def identify_all_command(clean_words):
    #identify all command base on keyword listed (check tool_list.py for futher information)
    if not clean_words:
        return []
    command_list = []
    for pos,word in enumerate(clean_words):
        for command,keywords in command_types.items():
            if word in keywords :
                command_list.append({"command":command ,
                                     "keyword":word         , 
                                     "pos"    :pos 
                                    })
    return command_list
def extract_commands(words):
    #seperate commands
    clean_words = clean_word(words)
    command_list = identify_all_command(clean_words)
    for i,command in enumerate(command_list) :
        current_pos = command["pos"]
        if i + 1 < len(command_list) :
            next_pos    = command_list[i+1]["pos"]
            command["argument"] = clean_words[current_pos+1: next_pos]
        else :
            command["argument"] = clean_words[current_pos+1:]
    return command_list
def clean_word(words):
    # Remove unnecesorry (!?,.:;) and connectors
    clean_words = []
    clean_words = [word.strip("!?,.:;") for word in words]
    clean_words = [word for word in clean_words if word not in connecter_list ]
    return clean_words
def check_valid(command_list):
    for command in command_list :
        if not command["argument"]:
            raise ValueError(f"Every command must have valid application")
    return True 
def command_router(transcript) :
    if not isinstance(transcript, str) or not transcript.strip():
        raise ValueError(f"Empty input")
    words = transcript.lower().split() 
    command_list = extract_commands(words) 
    if not command_list:
            raise ValueError("No valid command type found.")
    try:
        check_valid(command_list)
    except ValueError as e :
        print(e)
        raise 
    for command in command_list:
        for argument in command["argument"] :
            execute_tool(command["command"], argument)
        
    
    
    
