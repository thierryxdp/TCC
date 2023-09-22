def lingua_p(palavra):
    '''retorna uma palavra traduzida para a lingua do p
    str -> str'''
    str.lower(palavra)
    traducao = ''
    for i in palavra:
        if i in 'aeiouàáâãéêóôõ':
            traducao = traducao + i + 'p'
        if i in 'bcdfghjklmnpqrstvwxyz':
            traducao = traducao + i
    return traducao