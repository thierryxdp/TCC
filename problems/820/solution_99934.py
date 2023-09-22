def posLetra(texto,letra,numero):
    """Função que recebe uma string, uma letra e um número que indica a ocorrência desejada da letra e retorna em que posição da string aquela corrência está
    entrada: str, str, int
    saída: int"""
    i=0
    cont=0
    while cont<numero:
        if texto[i]==letra:
            cont=cont+1
            i=i+1
        elif:
            i=i+1
        if i>len(texto):
        	return -1
    return i-1