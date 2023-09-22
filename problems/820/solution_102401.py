def posLetra(string, letra, n):
    """funcao que indica a ocorrencia desejada de uma letra e retorna em que posicao da string a letra está.
    Se existir menos ocorrencia que a pedida retorna -1. 
    str, str, int -> int"""
    contagem = 0
    modificada = string
    original = string
    if str.count(string, letra)<n:
        return -1
    while contagem<n:
        x = str.index(modificada, letra)
        modificada = modificada[x+1:]
        contagem+=1
        
    return len(original)-len(modificada)-1