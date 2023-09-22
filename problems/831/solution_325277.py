def lingua_p(palavra):
    palavra.split()
    for i in range(0, len(palavra)):
        if palavra[i] in 'aeiouAEIOU':
            palavra.insert('p'+ palavra[i], palavra[i])
    return palavra.join()