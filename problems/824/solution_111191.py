def uppCons(texto):
    """funcao que recebe uma string e retorna essa string com todas as consoantes
    em maiusculos, e os demais caracteres do jeito original. string->string"""
    consoantes=()
    proximo=0
    while proximo<len(texto):
        if texto[