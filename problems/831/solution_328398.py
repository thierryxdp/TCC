def lingua_p(frase):
    """"""
    traducao = ''
    frase    = str.lower(frase)
    for i in frase:
        if i in 'aáàãâeéèêiíìoòóôõuúù':
            traducao = traducao + i + 'p'+ i   
        else:
            traducao = traducao + i
    return traducao