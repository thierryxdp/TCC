def inverte(frase):
    '''funcao que possui uma frase e que retorne a outra frase que
    possua as mesmas palavras da frase de entrada na
    ordem inversa'''
    '''str -> str'''
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