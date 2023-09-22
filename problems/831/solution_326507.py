def lingua_p(string):
    ''' Função que traduz uma string qualquer para a língua do P. 
    str -> str'''
    for i in range(len(string)):
        if string[i] in 'AEIOUaeiou':
            x = str.split(string)
            y = 'p' + string[i]
            k = y.join(x[0:i], x[i+1:-1])
            t = str.upper(k)
    return t