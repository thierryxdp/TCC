def lingua_p(palavra):
    i=0
    for i in range(len(palavra)):
        if palavra[i] in 'aeiouAEIOU':
            palavra=palavra[:i]+"p"+palavra[i:]
        i=i+1
    return frase