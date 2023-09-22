def lingua_p (palavra):
    '''Funcao que, dada uma palavra em portugues, retorna esta mesma palavra traduzida para a lingua do P.
    str->str'''
    
    traducao = ''
    for i in palavra:
        if i in 'AEIOUaeiou':
            i = i +'p' + i
        traducao += i
        str.lower(traducao)
    return traducao