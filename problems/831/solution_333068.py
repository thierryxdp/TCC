def lingua_p(palavra):
    final = ''
    for letra in str.lower(palavra):
        final = final + 'letra'
        if letra in [a, e, i, o, u]:
            final = final + 'p'
    return final