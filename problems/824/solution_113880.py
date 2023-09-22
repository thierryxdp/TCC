def uppCons(frase):
    frase_at=str.split(frase)
    
    indice=0
    while indice <len(frase_at):
        if frase_at[indice] != ('a','e','i','o','u'):
            str.upper(frase_at[indice])
        indice=indice+1
        
    return str.join(frase_at,'')