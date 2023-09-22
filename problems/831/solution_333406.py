def lingua_p(palavra):
    var = palavra
    n = len(palavra)
    for x in palavra:
        if x == ('a','e','i','o','u'):
            var[x] = var[x]+'p'+var[x]
        return var