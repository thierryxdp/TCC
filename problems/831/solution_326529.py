def lingua_p(string):
    ''' Função que traduz uma string qualquer para a língua do P. 
    str -> str'''
    i = 0
    while i < len(string):
        if string[i] in 'AEIOUaeiou':
            x = str.split(string, string[i])
            k = string[i] + 'p' + string[i]
            t = k.join(x)
            y = str.lower(t)
        i = i + 1
    return y