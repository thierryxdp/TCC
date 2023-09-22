def inverte(frase):
    """"Retirada da pontuação através do replace"""
    frase = frase.replace('-'," ")
    frase = frase.replace(':'," ")
    frase = frase.replace(','," ")
    frase = frase.replace(';'," ")
    frase = frase.replace('.'," ")
    frase = frase.replace('!'," ")
    frase = frase.replace('?'," ")
    lista_frase = frase.split(" ")
    
    return lista_frase