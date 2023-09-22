def posLetra(frase,letra,occ):
    i = 0
    ocorrencia = 0
    
    while i < len(frase):
        caractere = frase[i]
        
        if caractere == letra:
            ocorrencia += 1
        if ocorrencia == occ:
            return i
        i += 1
    return -1