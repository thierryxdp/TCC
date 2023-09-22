def lingua_p(palavra):
    P = ''
    for i in palavra:
        if i not in 'aeiouáéíóú':
            P += i
        if i in 'aeiouáéíóú':
            P += i+'p'+i
    return P