def lingua_p (palavra):
    ling_p = ''
    for i in len(palavra):
        if palavra[i] in 'AEIOUaeiou':
            ling_p += palavra[i]+'pe'
        else:
            ling_p += palavra[i]
    return lower.ling_p