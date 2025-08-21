def reverse_string(s: str) -> str:
    """
    Returns the reverse of the given string.
    """
    return s[::-1]

# open Week 6 folder
# pytest "test_2\test_2.py"

# Test cases for reverse_string function

def test_1():
    assert reverse_string("ooe") == "eoo"

def test_2():
    assert reverse_string("Hello") == "olleH"

def test_3():
    assert reverse_string("Aoeilaeiepae") == "eapeiealieoA"

def test_4():
    assert reverse_string("8n934t7n6gewugy8rew8y9n34yergfui23843rt734r") == "r437tr34832iufgrey43n9y8wer8yguweg6n7t439n8"

def test_5():
    assert reverse_string("(⌐■_■) ¯\_(ツ)_/¯") == "¯/_)ツ(_\\¯ )■_■⌐("