def posLetra(texto, letra, n):
    """funcao que recebe como entrada uma string, uma letra e um numero e retorna em que posicao
    da string aquela ocorrencia de letra esta, caso exista menos ocorrencias da letra do que a
    ocorrencia pedida, a funcao retorna -1;
    str, str, int -> int"""
    i = 0
    lista = []
    while i<len(texto):
        lista = lista+[i,]
    i = i + 1
    if n > len(lista):
        return -1
    else:
        return lista[n-1]