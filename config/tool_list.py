from command.commands import open_application, close_application
                           
tools = {"open_application": open_application,
         "close_application": close_application,
        }
command_types ={
        "open application": {"open", "launch", "start", "run", "execute", "activate"},
        "close application": {"close", "exit", "quit", "terminate", "shut", "end", "stop"},
        
    }
commands = {
    "open application": "open_application",
    "close application": "close_application",
    
}