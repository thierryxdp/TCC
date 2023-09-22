def inverte(frase):
    """"Retirada da pontuação através do replace"""
    frase = frase.replace('-'," ")
    frase = frase.replace(':'," ")
    frase = frase.replace(','," ")
    frase = frase.replace(';'," ")
    frase = frase.replace('.'," ")
    frase = frase.replace('!'," ")
    frase = frase.replace('?'," ")
    frase = frase.split(" ")
    lista_frase = frase.join(",",frase)