def uppCons(frase):
    contador=0
    letra='bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    frasef=''
    while contador<len(frase):
        caractere=frase[contador]
        if caractere in letra:
            caractere=str.upper(caractere)
        frasef+= caractere
        contador+=1
    return frasef