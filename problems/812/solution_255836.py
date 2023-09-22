import re

def retira_pontuacao(texto):
    """Recebe um texto e substitui a pontuacao por espacos"""
    return " ".join(re.split("[—,-:;.?!]+", texto))