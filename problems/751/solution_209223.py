"""Retorna a quantidade de palavras de uma frase
    str->int"""
    frase=str.rstrip(frase)
    frase=str.lstrip(frase)
    lista=str.split(frase)
    return len(lista)