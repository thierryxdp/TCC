def lingua_p(palavra):
    palavra1= ''
    for e in palavra:
        if e not in 'AEIOUaeiou':
            palavra1 = palavra1 + e
        if e in 'AEIOUaeiou':
            palavra1 = palavra1 + e + 'p'
    return palavra1