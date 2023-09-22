def lingua_p(palavra):
    palavra = list(str.lower(palavra))
    vogais = "aeiou"
    for x in range(len(palavra)):
        if(palavra[x] in vogais):
            palavra.insert(x + 1, "p")
            palavra.insert(x + 2, x)
    return "".join(palavra)