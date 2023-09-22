def retira_pontuacao(frase) :
    """str -> str"""
    """recebe uma frase e retorna esta frase com as pontuações trocadas por espaços"""
    
    i1 = frase.replace('-',' ')
    i2 = i1.replace(',',' ')
    i3 = i2.replace(':',' ')
    i4 = i3.replace(';',' ')
    i5 = i4.replace('.',' ')
    i6 = i5.replace('?',' ')
    i7 = i6.replace('!',' ')
    i8 = i7.replace('_',' ')
    
    return i8

def inverte(frase) :
    """ str -> str"""
    """recebe uma frase e retorna ela invertida"""
    
    F = retira_pontuacao(frase)
    
    I = f.split[::-1]
    
    return I