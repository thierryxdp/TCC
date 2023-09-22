def inverte(frase):
    '''funcao que dada uma frase retorne outra frase que
    contenha as mesmas palavras da frase de entrada na
    ordem inversa'''
    '''str->str'''
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
    frase=list (reversed(frase))
    return (' '.join(frase))
		return frase