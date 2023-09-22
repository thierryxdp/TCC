def lingua_p(palavra):
    pal = ''
    for i in palavra:
        if i in 'aeiou':
            pal = pal + list.insert(palavra,i-1,p)
            pal = pal + list.insert(palavra,i+1,p)
    return pal