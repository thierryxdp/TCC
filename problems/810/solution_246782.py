def inverte (frase):
    '''
    função que dada uma frase devolve a mesma de tras para frente
    str -> str
    '''
    frase2 = frase.replace(',',' ')
    frase3 = frase2.replace('.',' ')
    frase4 = frase3.replace('!',' ')
    frase5 = frase4.replace('?',' ')
    frase6 = frase5.replace('-',' ')
    return format(frase6.split(::-1))