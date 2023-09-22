def lingua_p(palavra):
    '''dada uma palavra, retorna a mesma na lingua do p
    str -> str'''
    palavra = str.lower(palavra)
    final = ''
    for i in palavra:
        if i in 'aeiouáéíóúãà':
            final += i + 'p' + i
        else:
            final += i
    return final