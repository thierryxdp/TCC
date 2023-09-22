def lingua_p(palavra):
    string = ''
    for i in palavra:
        if palavra[i] in 'AEIOUaeiou':
            palavra = palavra + palavra[i] + 'p'
            string = string + palavra[i]
    return string