def inverte(frase):
    """..."""
    x = frase
    y = str.lower(x)
    a = list(y)
    a.reverse()
    c = ''.join(a)
def retira_pontuacao(c):
    """Dada uma frase, retorna a mesma frase com espaço no lugar dos caracteres de pontuação
    str -> str"""
    if "-" or "," or ":" or ";" or "!" or "?" or "." in x:
         return str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(c, "-", " "), ",", " "), ":", " "), ";", " "), "!", " "), "?", " "), ".", " ")