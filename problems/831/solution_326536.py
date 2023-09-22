def lingua_p(string):
    ''' Função que traduz uma string qualquer para a língua do P. 
    str -> str'''
    que_coisa = ''
    for i in range(len(string)):
        if string[i] in 'AEIOUaeiou':
            x = str.split(string, string[i])
            k = string[i] + 'p' + string[i]
            t = k.join(x)
            y = str.lower(t)
            que_coisa += y[i:]
    return que_coisa