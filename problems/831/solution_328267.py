def lingua_p(palavra):

    for i in palavra:
        if i in 'AEIOUaeiou':
            palavra = palavra[0:palavra.index(i) + 1] + 'p' + str(i) \
                      + palavra[palavra.index(i) + 1:]

    return palavra.lower()