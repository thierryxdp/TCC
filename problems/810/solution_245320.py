def inverte(frase): 
    """ Insira uma frase entre aspas e a funcao retornara a frase com as palavras invertidas"""
    """str -> str"""
    frase = frase.replace('—',' ')
    frase = frase.replace(',',' ')
    frase = frase.replace(':',' ')
    frase = frase.replace('.',' ')
    frase = frase.replace(';',' ')
    frase = frase.replace('!',' ')
    frase = frase.replace('?',' ')
    frase = frase.replace('-',' ')
    frase = frase.lower()
    frase = frase.split()
    frase = list(reversed(frase))
    return (' '.join(frase))
    return frase