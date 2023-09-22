def conta_frases(texto):
    """conta o numero de frases terminadas por ".","!","?" ou "...""""
    
      frases = 0
    for i in range(len(texto)):
        if texto[i] == "!":
            frases += 1

        if texto[i] == "?":
            frases += 1

        if texto[i] == ".":
            if i != len(texto)-1 and (texto[i-1]=="." and texto[i+1]=="."):
                frases += 1
        
            if i != len(texto)-1 and (texto[i-1]!='.' and texto[i+1]!='.'):
                frases +=1
        
            if i == len(texto)-1 and texto[i-1] != '.':
                frases += 1
    return frases

    return(conta_frases(texto))