def lingua_p(palavra):
    i=0
    for n in palavra:
        if n in 'AEIOUaeiouéíóúáÉÍÓÚ':
            palavra=palavra[:i+1]+'p'+n+palavra[i+1:]
            i=i+2
        i=i+1
    return palavra