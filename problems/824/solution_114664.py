def uppCons(frase):
    contador=0
    letra= 'bçcdjklmnpqrstvwxyzBCÇDFGHJKLMNPQRSTVWXYZ'
    frafinal=''
     caractere=frase[contador]
    while contador<len(frase):
        if caractere in letra:
            caractere=str.upper(caractere)
            frafinal+=caractere
            contador+=1
            return frafinal