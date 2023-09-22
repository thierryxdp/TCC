def lingua_p(palavra):
    '''Função que traduz uma palavra para a língua do P;
    string -> string'''
    P = ''
    for i in palavra:
        if i not in 'aeiouáéíóú':
            P += i
        if i in 'aeiouáéíóú':
            P += i+'p'+i
    return P