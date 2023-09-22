def lingua_p(palavra):
    i=0
    for n in palavra:
        if n in 'AEIOUaeiou':
            palavra=palavra[:i]+'p'+n+palavra[i:]
        i=i+1
    return palavra