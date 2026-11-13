from command.commands import open_application, close_application, special_command
                            #,save_file, delete_file, get_file
tools = {"open_application": open_application,
         "close_application": close_application,
         "special_command": special_command
        }
command_types ={
        "open application": {"open", "launch", "start", "run", "execute", "activate"},
        "close application": {"close", "exit", "quit", "terminate", "shut", "end", "stop"},
        "special command": {"Hey"}
    }
commands = {
    "open application": "open_application",
    "close application": "close_application",
    "special command": "special_command",
}