def lingua_p(palavra):
    P = ''
    for i in palavra:
        if i != 'aeiou':
            P += i
    if i == 'aeiou':
        P += i+'p'+i
    return P