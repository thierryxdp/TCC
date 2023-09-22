def lingua_p(p):
    palavra = list(str.lower(p))
    i=0
    while i < len(palavra):
        if palavra[i] == 'aeiou':
            list.insert(palavra,i+1,'p')
        i=i+1
    return str(palavra)