def lingua p (palavra):
    '''recebe uma palavra (em português) e retorna'''
    '''str->str'''
    mini = str.lower (palavra)
    vogal = 'aeiouáéíóúáêôão¹
    final=''
    for letra in mini:
    if letra in vogal: final+= letra + 'p' + letra

    else:
    final + letra

    return final