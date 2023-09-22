def lingua_p(string):
    ''' Função que traduz uma string qualquer para a língua do P. 
    str -> str'''
    for i in range(len(string)):
        if string[i] in 'aeiouAEIOU':
            x = str.split(string, string[i])
            k = string[i] + 'p' + string[i]
            t = k.join(x)
            y = str.lower(t)
    return y