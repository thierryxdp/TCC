def posLetra(frase, letra, numero):
    '''função que conta quantas vezes uma letra apareceu
    em determinada ocorrência
    str, str, int--> int
    '''
    
    palavras = list(frase)

    contador = 0
    ocorrencias = 0
    
    while len(palavras) > contador:
        
        if letra in palavras[contador]:
            ocorrencias += 1
            
            if ocorrencias == numero:
                return contador
            
        contador += 1

    return ocorrencias