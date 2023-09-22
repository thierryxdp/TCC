def lingua_p(palavra):
    '''Função que recebe uma palavra em português como entrada e 
    retorna a palavra traduzida para língua do p
    str -> str'''
    n= str.lower(palavra)
    traducao= ''
    for x in n:
        if x in 'aeiou':
            traducao= traducao + x + 'p' + x
        else: 
            traducao= traducao + x
    return traducao