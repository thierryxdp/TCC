def lingua_p(palavra):
    t = ''
    palavra = palavra.lower()
    for i in palavra:
        if i in 'aeiou':
            t = t + 'p' + i + 'p'
        else:
            t = t+i
    return t