def lingua_p(palavra):
    var = palavra
    n = len(palavra)
    for x in palavra:
        if x == 'a':
            var[x] = 'a'+'p'+'a'
        return var