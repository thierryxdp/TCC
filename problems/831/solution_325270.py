def lingua_p(palavra):
    i=0
    for c in palavra:
        if c in 'aeiou':
            palavra=c+'p'+c
    i=i+1
    return palavra