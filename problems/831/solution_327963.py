def lingua_p(frase):
    for i in frase:
        frase.replace('a','ap')
        frase.replace('e','ep')
        frase.replace('i','ip')
        frase.replace('o','op')
        frase.replace('u','up')
        return frase