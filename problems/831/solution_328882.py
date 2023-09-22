def lingua_p (palavra):
    '''recebe uma palavra(em português) e retorna a mesma palavra traduzida para a língu do P'''
    '''str->str'''
    mini = str.lower (palavra)
    vogal = 'aeiouáéíóúâêôãõ'
    final= ''
    for letra in mini:
        if letra in vogal:
            final+= letra + 'p' + letra
        else:
            final += letra
            
    return final