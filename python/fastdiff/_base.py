from difflib import Differ

def compare(first, second):
    differ = Differ()
    return list(differ.compare(first.splitlines(), second.splitlines()))
