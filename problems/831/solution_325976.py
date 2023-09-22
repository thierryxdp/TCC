def lingua_p(palavra):
    P = ''
    for i in palavra:
        if i not in 'aeiou':
            P += i
        if i in 'aeiou':
            P += i+'p'+i
    return P