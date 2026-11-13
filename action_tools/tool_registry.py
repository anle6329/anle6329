from config.tool_list import tools
import typing
def register_tool(tool_name:str , tool_function:typing.Callable):
    if tool_name in tools:
        raise ValueError(f"Tool '{tool_name}' is already registered with function '{tool_function.__name__}'.")
    tools.update({tool_name: tool_function})
def get_tool(tool_name:str):
    if tool_name not in tools:
        raise ValueError(f"Tool '{tool_name}' is not registered.")
    return tools[tool_name]
def execute_tool(tool_name:str , *args, **kwargs):
    tool_function = get_tool(tool_name)
    return tool_function(*args, **kwargs)