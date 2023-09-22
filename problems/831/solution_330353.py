def lingua_p(palavra):
    string = ''
    a = 1
    for i in palavra:
        if palavra[i-a] in 'AEIOUaeiou':
            string = string + palavra[i]+'p'
    return string