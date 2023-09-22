def lingua_p (palavra):
    ling_p = ''
    i = 0
    for i in len(palavra):
        if palavra[i] in 'AEIOUaeiou':
            ling_p += palavra[i]+'pe'
        else:
            ling_p += palavra[i]
        i+=1
    return lower.ling_p