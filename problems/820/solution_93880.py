def posLetra(texto, letra, numero):
    """Função que recebe uma string, uma letra e um numero, indicando a ocorrencia
    desejada da letra, retornando a posição da string daquela ocorrencia de letra
    entra: str, str, int
    retorno: int"""
    i=0
    vezes=0
    for i in range(len(texto)):
        if texto[i]== letra:
            vezes=vezes + i
        is vezes == numero:
           return i
    if pos < numero:
        return -1