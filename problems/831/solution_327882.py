def lingua_p(palavra):
    for i in palavra:
        if i in 'AEIOUaeiou':
            palavra[i] + 'pe'
    return palavra