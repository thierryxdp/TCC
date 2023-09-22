def replace_punctuation(text):
    return text.replace(".", "").replace(",", "").replace("!", "").replace("?", "").replace(":", "").replace(";", "")

def inverte(frase):
    return list(reversed(replace_punctuation(frase).split(" "))).join(" ")