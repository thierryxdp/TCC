def lingua_p (palavra):
    ling_p = ''
    for i in range (len(palavra)):
        if palavra[i] in 'AEIOUaeiouáéóú':
            ling_p += palavra[i]+'p' + palavra[i]
        else:
            ling_p += palavra[i]
    return ling_p.lower()