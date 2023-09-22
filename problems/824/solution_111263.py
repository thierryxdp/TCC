def uppCons(frase):
    """
    Recebido uma frase de parametro, retorne a frase com todas as 
    consoantes em maiúsculo.
    Parametro de entrada: string
    Valor de saida: string
    
    """
    frase_CONSOANT=''
    i=0
    while i<len(frase):
        if frase[i] not in 'aáâãeéiíoóõôuú':
            frase_CONSOANT += str.upper(frase[i])
        else:
            frase_CONSOANT += frase[i]    
        i=i+1
    return frase_CONSOANT