def lingua_p(palavra):
    var = palavra
    n = len(palavra)
    for x in palavra:
        if x == 'a'or'e'or'i'or'o'or'u':
            var[x] = var[x]+'p'+var[x]
        return var