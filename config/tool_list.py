from command.commands import open_application, close_application
                            #,save_file, delete_file, get_file
tools = {"open_application": open_application,
         "close_application": close_application,
         #"save_file": save_file,
         #"get_file": get_file,
         #"delete_file": delete_file
        }
command_types ={
        "open_application": {"open", "launch", "start", "run", "execute", "activate"},
        "close_application": {"close", "exit", "quit", "terminate", "shut", "end", "stop"},
        
    }
commands = {
    "open application": "open_application",
    "close application": "close_application",
    
}