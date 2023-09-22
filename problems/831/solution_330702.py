def lingua_p(palavra):
    palavra = list(str.lower(palavra))
    vogais = "aeiou"
    for x in range(len(palavra)):
        if(palavra[x] in vogais):
            palavra.insert("p", x + 1)
            palavra.insert("x", x + 2)
    return "".join(palavra)