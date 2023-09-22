def lingua_p(palavra):
    s = ""
    for x in range(0,len(palavra)+1):
        if palavra[x] in 'AEIOUaeiou':
            s + str(x)
            s + str('p')
            s + str(x)
        elif palavra[x] not in 'AEIOUaeiou':
            s + str(x)
    return s