def retira_pontuacao(frase):
    """Dada uma frase, retorna a mesma frase com espaço no lugar dos caracteres de pontuação
    str -> str"""
    if "-" or "," or ":" or ";" or "!" or "?" or "." in x:
        return str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase, "-", " "), ",", " "), ":", " "), ";", " "), "!", " "), "?", " "), ".", " ")