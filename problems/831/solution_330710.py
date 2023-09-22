def lingua_p(palavra):
    palavra = list(str.lower(palavra))
    vogais = "aeiou"
    final = []
    for x in range(len(palavra)):
        final.append(palavra[x])
        if(palavra[x] in vogais):
            palavra.append("p")
            palavra.append(palavra[x])
    return "".join(final)