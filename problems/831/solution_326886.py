def lingua_p(palavra):
    i = 0
    while (i < len(palavra)):
        if  (str.lower(palavra[i]) in 'aeiou'):
            palavra = palavra.replace(palavra[i],'p' + palavra[i])
        i += 1
    return palavra