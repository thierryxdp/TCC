def lingua_p(palavra):
    for 'aeiou' in palavra:
        palavra.replace('a','ap')
        palavra.replace('e','ep')
        palavra.replace('i','ip')
        palavra.replace('o','op')
        palavra.replace('u','up')
        return palavra