def lingua_p(frase):
    """"""
    traducao = ''
    frase    = str.lower(frase)
    for i in frase:
        if i in 'aeiou':
            traducao = traducao + i + 'p'+ i   
        else:
            traducao = traducao + i
    return traducao