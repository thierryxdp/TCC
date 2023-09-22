def lingua_p(palavra):
    i = 0
    palavrap = ''
    while i < len(palavra):
        if palavra[i].lower in 'aeiou':
            palavrap += palavra[i] + 'p' + palavra[i]
        else:
            palavrap += palavra[i]
        i += 1
        return palavrap.lower