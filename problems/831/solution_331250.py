def lingua_p(palavra):
    '''Função que, ao receber uma palavra em português,
    retorna ela traduzida para a língua do p, a qual a cada 
    vogal é inserida a sequencia de letras 'p' mais a vogal
    original
    str -> str'''
    traducao = ''
    for i in palavra:
        if i in 'aeiouAEIOUíÍáÁúÚéÉ':
            traducao = traducao + i + 'p' + i
        else:
            traducao = traducao + i
    return traducao