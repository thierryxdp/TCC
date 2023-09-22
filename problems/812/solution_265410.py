def mulipleReplace(text):
    return "".join([char if char in ".!?," else "" for char in text)