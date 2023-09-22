def lingua_p(palavra):
    string = ''
    for i in palavra:
        if palavra[i] in 'AEIOUaeiou':
            str.append(palavra[i], 'p')
    return string