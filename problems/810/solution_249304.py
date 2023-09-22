def replace_punctuation(text):
    return text.replace(".", "").replace(",", "").replace("!", "").replace("?", "").replace(":", "").replace(";", "")

def inverte(frase):
    return replace_punctuation(text).split(" ").reverse()