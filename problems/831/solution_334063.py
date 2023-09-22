def lingua_p(string):
    '''Função traduz uma string para língua do p
       str --> str'''
    palavra = str.lower(string)
    p = []
    for i in string:
        if i in 'aeiouáéíóúàèìòù':
            p.append(i + 'p' + i)
        else:
            p.ppend(i)
    return ''.join(p)