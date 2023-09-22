uppCons (frase):
    """função que dado uma frase ela retorna a frase com todas as consoantes em maiúsculo 
    entrada->str
    retorna->str"""
    
    consoantes= 'bcdfghjklmnpqrstvwxyz'
    TMfrase= len (frase)
    indice=0
    
    while indice <TMfrase:
        if frase [indice] in consoantes:
            str.upper (frase,indice)
            indice=indice+1
    return frase