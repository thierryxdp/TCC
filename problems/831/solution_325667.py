def lingua_p(palavra):
    i=0
    volgar=' '
    while i<len(palavra):
        if palavra[i] in 'AEIOUaeiou':
            vogal=palavra + 'p'
        i=i+1
    return vogal