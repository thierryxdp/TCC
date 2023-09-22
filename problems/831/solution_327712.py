def lingua_p(palavra):
    alterado=palavra
    for i in range(len(palavra)):
        if alterado[i] in 'aeiou':
            p=(alterado[:i] + 'p' )
        alterado+= p
    return alterado