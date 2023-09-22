def lingua_p(palavra):
    i=0
    while i<len(palavra):
        if palavra[i] in 'aeiouAEIOU':
            palavra=palavra[:i]+"p"+palavra[i:]
        i=i+1
    return frase