def lingua_p (palavra):
    ''' '''
    ''' '''
    mini = str.lower (palavra)
    vogal = 'aeiouáéíóúâêôãõ'
    final= ''
    for letra in mini:
        if letra in vogal:
            final+= letra + 'p' + letra
        else:
            final += letra
            
    return final