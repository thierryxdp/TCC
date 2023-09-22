def lingua_p(string):
    ''' Função que traduz uma string qualquer para a língua do P. 
    str -> str'''
    string_nova = []
    for i in string:
        if i in 'aeiouAEIOU':
            string = string.lower()
            string_nova = string_nova + [i] + ['p'] + [i]
        else:
            string_nova + string_nova = string
    return ''.join(string_nova)