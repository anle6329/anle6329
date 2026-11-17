import pytest
from command.commands_router import extract_commands , check_valid , clean_word , command_router
def test_word_cleaning() :
    test_text = [
        "spotify!!!!!" ,
        "Chrome?????"
    ]
    res = []
    for item in test_text:
        res.extend(clean_word(item))
    assert res == ["spotify","chrome"]
def test_extracting_single_command() :
    test_text = "open spotify"
    res = extract_commands(test_text)
    assert res == [
        {
        "command": "open_application",
        "keyword": "open",
        "pos": 0,
        "argument": ["spotify"],
        }
    ]
def test_extracting_multiple_commands() :
    test_text = "open chrome then close spotify"
    res = extract_commands(test_text)
    assert res == [
        {
        "command": "open_application",
        "keyword": "open",
        "pos": 0,
        "argument": ["chrome"],
        },
        {
        "command": "close_application",
        "keyword": "close",
        "pos": 2,
        "argument": ["spotify"],
        }
        ]
def test_extracting_multiple_arguments():
    test_text = "open chrome and spotify" 
    res = extract_commands(test_text)
    assert res == [
            {
            "command": "open_application",
            "keyword": "open",
            "pos": 0,
            "argument": ["chrome","spotify"],
            }
        ]
def test_check_valid_punctuation_only():
    test_text = "open !!!!"
    command = extract_commands(test_text)
    with pytest.raises(ValueError):
        check_valid(command)
    
def test_valid_rejects_missing_arguments():
    command = [{"command": "open_application", "argument": []}]

    with pytest.raises(ValueError):
        check_valid(command)
def test_valid_sufficient_arguments():
    command = [{"command": "open_application", "argument": ["spotify"]}]
    check_valid(command)
def test_reject_empty_input() :
    input = ""
    with pytest.raises(ValueError):
        command_router(input) 
def test_unrecognized_commands():
    input = "delete text.txt"
    with pytest.raises(ValueError):
        command_router(input)
