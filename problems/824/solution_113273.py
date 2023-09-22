def uppCons(frase):
    """função que coloca as consoantes em letra maiusculas
    str -> str"""
    i = 0
    texto2=''
    while i < len(frase):
        if frase[i] in 'aeiouáéíóúâêîôûã': 
            texto2 = texto2 + frase[i]
        else:
            texto2 = texto2 + str.upper(frase[i])
        i = i +1
        
    return texto2