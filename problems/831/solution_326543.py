def lingua_p(string):
    ''' Função que traduz uma string qualquer para a língua do P. 
    str -> str'''
    for i in string:
        if i in 'aeiouAEIOU':
            x = str.split(string, string[i])
            k = [i] + 'p' + [i]
            t = k.join(x)
            y = str.lower(t)
    return y