def lingua_p(palavra):
    '''dada uma palavra em português, retorna a tradução para a lingua do p;
    str --> str'''
    modelo=''
    for letra in palavra:
        if letra not in 'bcçdfghjklmnpqrstvwxyzBCÇDFGHJKLMNPQRSTVWXYZ':
            modelo=modelo+letra+'p'+letra
        else:
            modelo=modelo+str.lower(letra)
    return modelo