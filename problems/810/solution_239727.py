def inverte(frase):
    """"Retirada da pontuação através do replace"""
    frase = frase.replace('-'," ")
    frase = frase.replace(':'," ")
    frase = frase.replace(','," ")
    frase = frase.replace(';'," ")
    frase = frase.replace('.'," ")
    frase = frase.replace('!'," ")
    frase = frase.replace('?'," ")
    """Transformação das palavras em lista pelo separador " """"
    lista_frase = frase.split(" ")
    final = str.join('',lista_frase[-50:-1])
    return final