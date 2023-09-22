def lingua_p(palavra):
    s = ""
    proximo = 0
    while proximo < len(palavra):
        if palavra[proximo] in 'AEIOUaeiou':
            s + str(palavra[proximo])
            s + str('p')
            s + str(palavra[proximo])
        elif palavra[proximo] not in 'AEIOUaeiou':
            s + str(palavra[proximo])
    return s