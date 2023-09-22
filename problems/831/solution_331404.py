def lingua_p(palavra):
    '''Função que recebe uma palavra em português e retorna ela traduzida para a língua do p
    str -> str'''
    traducao = ''
    for i in palavra:
        if i in 'aeiouAEIOUíÍáÁúÚéÉ':
            traducao = traducao + i + 'p' + i
        else:
            traducao = traducao + i
    return traducao