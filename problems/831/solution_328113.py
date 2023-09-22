def lingua_p(palavra):
    vogais = ['A','E','I','O','U','a','e','i','o','u']
    palavra = list(palavra)
    index = 0
    for i in palavra:
        if i in vogais:
            palavra.insert(index,palavra[0:index+1])
        index += 1
    return "".join(palavra)