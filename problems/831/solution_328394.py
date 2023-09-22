def lingua_p(palavra):
    '''Função que recebe uma palavra em português e retorna a palavra
    traduzida para a língua do P.
    str -> str'''
    
    palavra1 = ''
    palavra2 = ''
    
    for m in list(palavra):
        if m in 'aeiouAEIOU':
            palavra1 = m + 'p' + m
        else:
            palavra1 = m
    	palavra2 = palavra2 + palavra1
    return str.lower(palavra2)