def lingua_p(string):
    ''' Função que traduz uma string qualquer para a língua do P. 
    str -> str'''
    que_coisa = ''
    for i in range(len(string)):
        if string[i] in 'AEIOUaeiou':
            y = 'p' + string[i]
            k = string[:i+1] + y + string[i+1:]
            que_coisa += k
            t = str.lower(que_coisa)
    return t