def posLetra(texto, letra, numero):
    """Função que recebe uma string, uma letra e um numero, indicando a ocorrencia
    desejada da letra, retornando a posição da string daquela ocorrencia de letra
    entra: str, str, int
    retorno: int"""
    i=0
    while i < len(texto):
        if texto[i]== letra:
            pos=i
        i=i + 1
    if pos < numero:
        return -1
    return pos