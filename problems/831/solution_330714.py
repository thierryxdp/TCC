def lingua_p(palavra):
    '''Função que retorna a palavra de entrada traduzida para a
    lingua p
    str -> str'''
    p = ''
    for i in palavra:
        if i in  'AEIOUaeiouáéíóú':
            p = p + i + 'p' + i
        else:
            p = p + i
    return p