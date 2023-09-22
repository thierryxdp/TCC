def lingua_p(palavra):
    for e in palavra:
        if e in 'AEIOUaeiou':
            return str.join('p', e, e)