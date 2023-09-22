def uppCons(frase):
    contador=0
    letra ='bcdfghjklmnpqrstvxwyzç'
    frase_final=''
    while contador<len(frase):
          caractere=frase[contador]
        if caractere in letra:
            caractere=frase[contador]
            caractere= str.upper(caractere)
            frase_final=frase_final+caractere
            contador=contador + 1
    return frase_final