def lingua_p(frase):
    for i in frase:
        if i in 'aeiou':
            frase.replace('a','ap')
            frase.replace('e','ep')
            frase.replace('i','ip')
            frase.replace('o','op')
            frase.replace('u','up')
        return frase