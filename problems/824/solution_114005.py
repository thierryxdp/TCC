def uppCons(frase):
    frase_at=''
    indice=0
    while indice < len(frase):
        if frase[indice] != 'a,e,i,o,u':
            x= str.upper(frase[indice])
            frase_at= frase_at + x
        else:
            frase_at= frase_at + frase[indice]
            
        indice= indice+1    
    return frase_at