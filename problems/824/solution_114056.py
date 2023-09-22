def uppCons(frase):
    frase_at=''
    indice=0
    while indice < len(frase):
        if frase[indice] != 'a' and  frase[indice] != 'á' and  frase[indice] != 'ã' and  frase[indice] != 'e' and  frase[indice] != 'é' and frase[indice] != 'i' and frase[indice] != 'í' and frase[indice] != 'o' and frase[indice] != 'ó' and frase[indice] != 'õ' and frase[indice] != 'u' and frase[indice] != 'ú': 
            x= str.upper(frase[indice])
            frase_at= frase_at + x
        else:
            frase_at= frase_at + frase[indice]
            
        indice= indice+1    
    return frase_at