def lingua_p(palavra):
    '''recebe uma palavra e onde tem vogal, acrescenta um 'p' e novamente a mesma vogal.
    str -> str'''
    min_palavra = str.lower(palavra)
    pos = 0
    for vogal in min_palavra:
        if min_palavra[pos] in 'aeiou':
            resultado = min_palavra[:pos] + vogal + 'p' + min_palavra[pos:]
        pos = pos + 1
    return resultado