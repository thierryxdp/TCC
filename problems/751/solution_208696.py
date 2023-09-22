def quant_palavras(frase):
    """A função recebe uma frase e retorna o numero de palavras dela. Para isso, a função separa
    a frase em uma lista, denominada 'a' por conveniência, com várias substrings, através do str.split com o ' ' como separador.
    Essas substrings são as palavras da frase original. Então separa-se os '' que são gerados pelo str.split
    caso exista espaço inicial ou final na frase e, então, calcula o tamanho da lista, usanado o len
    pois cada palavra é um indice da lista 'a'.; Str -> Int"""
    a = str.split (frase, ' ')
    if '' in a:
        list.remove (a, '')
    return len(a)