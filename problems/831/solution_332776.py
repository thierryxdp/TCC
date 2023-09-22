def lingua_p(palavra):
    for e in palavra:
        if e in 'AEIOUaeiou':
            str.join('p', e)
    return palavra