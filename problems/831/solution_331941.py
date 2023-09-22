def lingua_p(palavra):
    i = 0
    palavrap = ''
    while i < len(palavra):
        if str.lower(palavra[i]) in 'aeiou':
            palavrap += palavra[i] + 'p' + palavra[i]
        else:
            palavrap += palavra[i]
            i += 1
        return palavrap.lower