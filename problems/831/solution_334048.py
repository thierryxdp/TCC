def lingua_p(palavra):
    b=''
    for i in range (len(palavra)):
        if palavra[i] in 'aeiouAEIOU':
            b=b+palavra[i]
    return str.lower(palavra)