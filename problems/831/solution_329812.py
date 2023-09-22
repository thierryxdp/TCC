def lingua_p(p):
    '''Essa função ao receber como valor de entrada uma string(em português), ela retornara esta mesma palavra traduzida para a língua do P'''
    ''' str->str'''
    mini = str.lower (palavra)
    vogal = 'aeiouáéíóúâêôãõ'
    final= ''
    for letra in mini:
        if letra in vogal:
            final+= letra + 'p' +letra
        else:
            final += letra
            
    return final