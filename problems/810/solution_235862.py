import re

def inverte(frase):
    """Remove a pontuacao e inverte a ordem das palavras de uma frase"""
    return " ".join(" ".join(re.split("[—,-:;.?!]+", frase)).split(" ")[::-1])