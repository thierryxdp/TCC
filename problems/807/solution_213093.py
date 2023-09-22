def conta_frases(texto):
    '''Calcula o numero de frases presentes em um texto, string
       parameters:
       texto: string qualquer
       str -> str'''
    return len(str.split(texto,['.','!','?','...']))