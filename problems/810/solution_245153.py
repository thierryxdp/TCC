def inverte (frase):
    '''recebe uma frase, calcula  e retorna uma frase onde os caracteres de pontuação são substituídos por espaço e depois a ordem da frase é invertida'''
    '''str->str'''
    um =  str.replace (frase,'-',' ')
    dois =  str.replace (um,',',' ')
    tres = str.replace (dois ,':',' ')
    quatro = str.replace (tres,';',' ')
    quinto = str.replace (quatro, '.',' ')
    sexto = str.replace (quinto, '!',' ')
    setimo = str.replace (sexto, '?',' ')
    semponto = setimo

    minusculas = str.lower (semponto)
    
    split = str.split (minusculas)
    return ' '.join (split[::-1])