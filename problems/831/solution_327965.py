def lingua_p(frase):
    for i in frase:
        if i in 'aeiou':
            frasx = frase.replace('a','ap')
            frasx = frase.replace('e','ep')
            frasx = frase.replace('i','ip')
            frasx = frase.replace('o','op')
            frasx = frase.replace('u','up')
        return frasx