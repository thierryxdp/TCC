def lingua_p(palavra):
    pal = ''
    for i in palavra:
        if i in 'aeiou':
            pal = pal + list(palavra.insert(i-1,p))
            pal = pal + list(palavra.insert(i+1,p))
    return pal