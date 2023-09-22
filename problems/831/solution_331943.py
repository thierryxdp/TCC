def lingua_p(palavra):
    i = 0
    palavrap = ''
    while i < len(palavra):
        if str.lower(palavra[i]) in 'aeiou':
            palavrap += str(palavra[i]) + 'p' + str(palavra[i])
        else:
            palavrap += str(palavra[i])
        i += 1
        return str.lower(palavrap)