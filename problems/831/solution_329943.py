def lingua_p (palavra):
    '''str -> str'''
    mini = str.lower(palavra)
    vogal = 'aeiouáéíóúãõâêô'
    final = ''
    for letra in mini:
        if letra in vogal:
            final += letra + 'p' + letra
        else:
            final += letra
            
    return final