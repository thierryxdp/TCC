def lingua_p(str):
    '''Função traduz uma string para língua do p
       str --> str'''
    string = str.lower(string)
    p = []
    for i in string:
        if i in 'aeiouáéíóúàèìòù':
            p.append(i + 'p' + i)
        else:
            p.ppend(i)
    return ''.join(p)