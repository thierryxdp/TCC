def lingua_p(palavra):
    for d in palavra:
        if d in 'AEIOUaeiou':
            palavra=str.replace(palavra,d,d+'p')
    return palavra