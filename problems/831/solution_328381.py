def lingua_p(palavra):
    '''Função que recebe uma palavra em português e retorna a palavra
    traduzida para a língua do P.
    str -> str'''
    
    palavra1 = ''
    
    for m in list(palavra):
        if m in 'AEIOUaeiou':
            palavra1 = palavra[m:m+1] + 'p' + str(m) + palavra[m+1:]
            
    return str.lower(palavra1)