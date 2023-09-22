def inverte(text):
    if len(text) <= 1:
        return text

    return inverte(text[1:]) + text[0]