def lingua_p(palavra):
    for x in palavra:
        if x in 'AEIOUaeiou':
            x = 'p' + x
    return palavra