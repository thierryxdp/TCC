def lingua_p(string):
    ''' Função que traduz uma string qualquer para a língua do P. 
    str -> str'''
    string_nova = []
    for i in string:
        if i in 'áéíóúãêîõôûaeiouAEIOU':
            string = string.lower()
            string_nova = string_nova + [i] + ['p'] + [i]
        else:
            string_nova = string_nova + [i]
    return ''.join(string_nova)