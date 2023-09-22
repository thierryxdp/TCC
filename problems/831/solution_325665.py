def lingua_p(palavra):
    i=0
    volgar=' '
    while i<len(palavra):
        if palavra[i] in 'AEIOUaeiou':
            vogal=palavra[i]
        i=i+1
    return vogal