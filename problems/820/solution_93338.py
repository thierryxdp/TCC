def posLetra ( texto, letra, numero):
    """ a funcao ira receber uma frase uma letra e uma posicao, essa posicao representa o numero que indica a ocorrencia desejada da letra
    entrada : str, str, int   saida: int"""
    
    i = 0
    indice = []
    
    if texto.count (letra) < numero:
        return -1
    
    while i<len (texto):
        if letra in texto [i]:
            list.append(indice,i)
        i = i + 1
    return indice [numero-1]