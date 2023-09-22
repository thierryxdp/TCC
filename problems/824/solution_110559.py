def uppCons(frase):
    """Função que transforma todas as consoantes da frase em maiuscula.
    str -> str"""
    i=0
    frase_maiuscula=''
    lista=list(frase)
    while i<len(frase):
        if lista[i] in "bcdfghjklmnpqrstvwyxzçBCDFGHJKLMNPQRSTVWYXZÇ":
            lista[i]=str.upper(lista[i])
        i=i+1
    frase_maiuscula=''.join(lista)
    return frase_maiuscula