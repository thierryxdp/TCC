def uppCons(frase):
    contador=0
    letra= 'bçcdjklmnpqrstvwxyzBCÇDFGHJKLMNPQRSTVWXYZ'
    frafinal=''
     while contador<len(frase):
             caractere=frase[contador]
        if caractere in letra:
            caractere=str.upper(caractere)
        frafinal+=caractere
        contador+=1
        
        return frafinal