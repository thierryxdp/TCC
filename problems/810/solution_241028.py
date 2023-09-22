def inverte (frase):
    '''Retorna a frase dada de forma inversa, sem letra maiúscula e sem pontuação'''
         #str->str
    if "." in frase:
        frase = frase.replace(".", " ")
    if "," in frase:
        frase = frase.replace(",", " ")
    if ";" in frase:
        frase = frase.replace(";", " ")
    if "!" in frase:
        frase = frase.replace("!", " ")
    if "?" in frase:
        frase = frase.replace("?", " ")
    if ":" in frase:
        frase = frase.replace(":", " ")
    if "-" in frase:
        frase = frase.replace("-", " ")
        
    frase_lista = frase.split(' ')
    numero_palavras = (len(frase_lista)+1)
    fatiamento_inverso = frase_lista[-1:-(numero_palavras):-1]
    inverte = str.join(' ',fatiamento_inverso)
                              
    return str.lower (inverte)