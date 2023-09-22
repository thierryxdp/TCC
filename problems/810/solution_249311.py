def replace_punctuation(text):
    return text.replace("-", " ").replace(".", "").replace(",", "").replace("!", "").replace("?", "").replace(":", "").replace(";", "")

def inverte(frase):
    return " ".join(reversed(replace_punctuation(frase).split(" ")))