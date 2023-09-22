def inverte (texto):
    ''' '''
    texto = texto.replace('-',' ')
    texto = texto.replace(',',' ')
    texto = texto.replace(':',' ')
    texto = texto.replace('!',' ')
    texto = texto.replace('...',' ')
    texto = texto.replace('?',' ')
    texto = texto.replace('.',' ')
    
    texto = texto.lower()
    texto = texto.split(' ')
    texto = texto.reverse()
    texto = texto.join
    
    return texto