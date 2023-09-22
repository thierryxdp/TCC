def inverte(frase):
    """"Retirada da pontuação através do replace"""
    frase = frase.replace(" "," ") 
    frase = frase.replace('-'," ")
    frase = frase.replace(':'," ")
    frase = frase.replace(','," ")
    frase = frase.replace(';'," ")
    frase = frase.replace('.'," ")
    frase = frase.replace('!'," ")
    frase = frase.replace('?'," ")
    frase = frase.lstrip()
    frase = frase.rstrip()
    """Transformação das palavras em lista pelo separador " """"
    lista_frase = frase.split(" ")

    """ concatenando a lista de trás pra frente em uma string"""
    final = str.join(" ",lista_frase[::-1])
    
    return final