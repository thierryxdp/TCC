def posLetra(string, letra, numero):
    """A função recebe uma string, uma letra e um número, e retorna qual a
    indexação da ocorrencia da letra na string, em relação ao numero (1 para
    a primeira ocorrência, 2 para a segunda, e assim por diante);
    str, str, int -> int"""
    i = 0
    lista = []
    if numero>str.count(string, letra):
        return -1
    while i<len(string):
        if string[i] == letra:
            lista.append(i)
        i = i +1
    return lista[numero-1]