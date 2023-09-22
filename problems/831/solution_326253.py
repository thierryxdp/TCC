def lingua_p(palavra):
    '''retorna a palavra traduzida para a lingua do P. string->string'''
    for i in palavra:
        if i in 'aeiouAEIOU':
            i+'p'+i
    return palavra