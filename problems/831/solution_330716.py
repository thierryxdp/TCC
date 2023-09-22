def lingua_p(palavra):
    '''Função que dada uma palavra em português, retorna essa mesma palavra traduzida na lingua do p:
    str -> str'''
    P = ' '
    for i in palavra:
        if i in 'aeiouàáéíóúAEIOUÁÉÍÓÚÀ':
            P = P + i + 'p' + i
        else:
            P = P + i
    return P