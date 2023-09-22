def lingua_p(palavra):
    """recebe uma palava (em português) e retorne esta mesma palavra traduzida
    para a língua do P
    str -> str"""
    traducao = ''
    for i in palavra:
        if i in 'aeiouAEIOUíÍáÁúÚéÉ':
            traducao = traducao + i + 'p' + i
        else:
            traducao = traducao + i
    return traducao