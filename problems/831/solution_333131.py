def lingua_p(palavra):
    '''Recebe uma palavra qualquer em português e a traduz para a língua do P.
    str->str'''
    p = str()
    for letra in palavra:
        if letra in 'aeiouáéíóúãõâêôAEIOUÁÉÍÓÚÂÊÔÃÕ':
            p = p+letra+'p'+letra
        else:
            p = p+letra
    return p