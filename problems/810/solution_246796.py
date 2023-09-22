def inverte (frase):
    '''
    função que dada uma frase devolve a mesma de tras para frente
    str -> str
    '''
    frase2 = frase.replace(',','')
    frase3 = frase2.replace('.','')
    frase4 = frase3.replace('!','')
    frase5 = frase4.replace('?','')
    frase6 = frase5.replace('-',' ')
    frase7 = str.split(frase6)
    frase8 = str(frase7[::-1])
    frase9 = frase8.replace("'","")
    frase10 = frase9.replace(',','')
    frase11 = frase10.replace('[','')
    frasefinal = frase11.replace(']','')
    return frasefinal