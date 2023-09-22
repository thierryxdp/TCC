import re

def inverte(frase):
    """Remove a pontuacao e inverte a ordem das palavras de uma frase"""
    return " ".join(re.split("[—,-:;.?!]+", texto)).split(" ")[::-1].join(" ")