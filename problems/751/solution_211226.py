def frase(frase):
    """Esta funcao recebe uma string e conta o numero de palavras nesta string
    str -> int"""
    numero_palavras = str.split(frase)
    return len(numero_palavras)