def inverte(frase):
    '''Função que recebe uma frase e que retorna esta frase com as palavras em 
    uma  ordem  inversa sem letra maiúsculas além de sem pontuação.
    str => str'''
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
    frase = (' '.join(frase))
    return frase