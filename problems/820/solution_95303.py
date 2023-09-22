def posLetra(frase,letra,num):
    """..."""
    ocorrencias = str.count(frase,letra)
    ocorrencias_atuais = 0
    posicao = 0
    
    while posicao < len(frase):
        if frase[posicao] == letra:
            ocorrencias_atuais = ocorrencias_atuais + 1 
        posicao = posicao + 1
        
    return posicao