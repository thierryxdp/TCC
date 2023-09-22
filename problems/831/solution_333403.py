def lingua_p(palavra):
    var = palavra
    n = len(palavra)
    for x in palavra:
        if x == 'aeiou':
            var[x] = var[x]+'p'+var[x]
        return var