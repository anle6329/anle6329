from command.commands import open_application, close_application
                           
tools = {"open_application": open_application,
         "close_application": close_application,
        }
command_types ={
        "open_application": {"open", "launch", "start", "run", "execute", "activate"},
        "close_application": {"close", "exit", "quit", "terminate", "shut", "end", "stop"},
        
    }
connecter_list ={
    "and"        , 
    "then"       ,
    "after"      ,
    "next"       ,
    "afterwards"
}