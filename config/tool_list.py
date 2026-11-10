from command.commands import open_application, close_application
                            #,save_file, delete_file, get_file
tools = {"open_application": open_application,
         "close_application": close_application,
         #"save_file": save_file,
         #"get_file": get_file,
         #"delete_file": delete_file
        }
command_types ={
        "open application": {"open", "launch", "start", "run", "execute", "activate"},
        "close application": {"close", "exit", "quit", "terminate", "shut", "end", "stop"},
        #"save file":{"save", "store", "record", "keep", "archive", "preserve", "stash"},
        #"get file":{"get", "retrieve", "fetch", "obtain", "acquire", "access"},
        #"delete file":{"delete", "remove", "erase", "clear", "discard", "extinguish", "destroy"}
    }
commands = {
    "open application": "open_application",
    "close application": "close_application",
    #"save file": "save_file",
    #"get file": "get_file",
    #"delete file": "delete_file"
}