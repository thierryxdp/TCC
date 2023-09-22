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
    
    return frase[-1]