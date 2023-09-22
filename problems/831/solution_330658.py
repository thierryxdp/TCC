def lingua_p(palavra):
    nova_palavra = ""
    p = ""
    for i in range(len(palavra)):
        if palavra[i] in 'AEIOUaeiou':
            p = p + "p" + palavra[i]
        nova_palavra = nova_palavra + p
    return nova_palavra