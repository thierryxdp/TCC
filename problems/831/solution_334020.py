def lingua_p(palavra):
    t = ''
    palavra = palavra.lower()
    for i in palavra:
        if i in 'aeiouáéóúàãõ':
            t = t + i+ 'p' + i
        else:
            t = t+i
    return t