import re

def inverte(frase):
    """Remove a pontuacao e inverte a ordem das palavras de uma frase"""
    return " ".join(re.split("\s+", " ".join(re.split("[—,-:;.?!]+", frase)))[-2::-1]).lower()