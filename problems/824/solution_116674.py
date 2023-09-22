def uppCons(frase):
    contador=0
    letra='bcçdfghklmnpqrstvwxyzBCÇDFGHJKLMNPQRSTVWXYZ'
    frasef="
    while contador<len(frase):
        caractere=frase[contador]
        if caractere in letra:
            caractere=str.upper(caractere)
        frasef+=caractere
        contador+=1
    return frasef