def lingua_p(palavra):
    '''Função que recebe uma palavra em português e retorna a palavra
    traduzida para a língua do P.
    str -> str'''
    
    palavra1 = ''
    palavra2 = ''
    
    for m in list(palavra):
        if m in 'aeiouAEIOU':
            palavra1 = palavra[str.index(palavra, m):str.index(palavra, m)+1] + 'p' + m
        else:
            palavra1 = palavra[:str.index(palavra, m)+1]
    	palavra2 = palavra2 + palavra1
    return str.lower(palavra2)