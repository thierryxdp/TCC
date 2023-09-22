def lingua_p(palavra):
    palavra1= ''
    for e in palavra:
        if e not in 'AEIOUaeiou':
            palavra1 = palavra1 + e
        if e in 'AEIOUaeiou':
            palavra1 = palavra1 + e + 'p' + e
    return palavra1