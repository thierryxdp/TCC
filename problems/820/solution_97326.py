def posLetra(frase,letra,numero):
    """funcao que aponta a posicao da letra na string de acordo com o numero,
       que representa a ocorrencia da çetra"""
    
    i=0
    ocorrencia=0
    
    while (i<len(frase)):
        if letra==frase[i]:
            ocorrencia=ocorrencia+1
            if ocorrencia == numero:
                return i
        i=i+1
    return -1