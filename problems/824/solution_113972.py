def uppCons(frase):
    frase_at=''
    indice=0
    while indice < len(frase):
        if frase[indice] != 'aeiou':
            str.upper(frase[indice])
           
            frase_at= frase_at + frase[indice]
        else :
            frase_at= frase_at + frase[indice]
            
        indice= indice+1    
    return frase_at