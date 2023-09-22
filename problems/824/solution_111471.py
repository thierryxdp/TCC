def uppCons(frase):
    """Função que transforma todas as consoantes da frase em maiuscula.
    str -> str"""
    i=0
    frase_cmaiuscula=''
    lista=list(frase)
    while i<len(frase):
        if lista[i] in "bcdfghjklmnpqrstvwyxzçBCDFGHJKLMNPQRSTVWYXZÇ":
            lista[i]=str.upper(lista[i])
        i=i+1
    frase_cmaiuscula=''.join(lista)
    return frase_cmaiuscula