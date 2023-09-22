def posLetra(texto,letra,numero):
    
    posicao = ()
    
    i = 0
    ocorrencia = 0
    
    while i < len (texto):
        
        if texto[i] == letra:
            posicao = i
            ocorrencia += 1
            if ocorrencia == numero:
            	return posicao
        i = i + 1
    return -1