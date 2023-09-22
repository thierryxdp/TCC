def lingua_p(palavra):
    nova_palavra = ""
    p = ""
    for i in range(len(palavra)):
        if palavra[i] in 'AEIOUaeiou':
            p = palavra[i] + "p" + palavra[i]
        nova_palavra = palavra[i] + p
    return nova_palavra