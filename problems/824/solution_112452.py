def uppCons (frase):
    """função que dado uma frase ela retorna a frase com todas as consoantes em maiúsculo 
    entrada->str
    retorna->str"""
    
    consoantes= 'bcdfghjklmnpqrstvwxyz'
    TMfrase= len (frase)
    indice=0
    N_frase=''
    
    while indice <TMfrase:
        if frase [indice] in consoantes:
            cons= str.upper (frase,indice)
            N_frase= N_frase+cons
            indice=indice+1
        else:
            N_frase=N_frase+frase [indice]
            indice=indice+1
    return N_frase