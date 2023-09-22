def uppCons(frase):
    
    indice=0
    frase_at=[]
    while indice <len(frase):
        if frase[indice] != ('a','e','i','o','u'):
            str.upper(frase[indice])
        indice=indice+1
    return frase