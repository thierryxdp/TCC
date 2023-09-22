def lingua_p(string):
    ''' Função que traduz uma string qualquer para a língua do P. 
    str -> str'''
    for i in range(0, len(string)):
        if string[i] in 'AEIOUaeiou':
            y = 'p' + string[i]
            k = string[:i+1] + y + string[i+1:]
            t = str.lower(k)
    return t