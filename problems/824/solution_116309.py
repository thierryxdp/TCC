def uppCons(frase):
    contador=0
    letra= 'bcdfghjklmnpqrstvxwyzç'
    frase_final=''
    while contador<len(frase):
        caractere=frase[contador]
        if caractere in letra:
            caractere=str.upper(caractere)
        frase_final+=caractere
        contador+=1
        
        
    return frase_final