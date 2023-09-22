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
        if frase[i] in 'bcdfghjklmnpqrstwxyz':
            frase_CONSOANT = frase_CONSOANT + str.replace(frase,frase[i],str.upper(frase[i]))   
        i=i+1
    return frase_CONSOANT