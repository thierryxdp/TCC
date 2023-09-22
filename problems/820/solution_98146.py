def posLetra(string, letra, numero):
    
    tamanho = len(string)
    
    i = 0
    
    contagem = str.count(string, letra)
    
    if contagem < numero:
        return -1
    
    indice = 0
    
    while True:
        if string[i] == letra:
            indice += 1
        if indice == numero:
            break
    return i