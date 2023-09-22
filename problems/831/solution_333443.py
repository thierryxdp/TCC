def lingua_p(palavra):
    var = palavra
    n = len(palavra)
    for x in range(1,n+1):
        if x == 'a':
            palavra.replace('a','apa')
        if x == 'e':
            palavra.replace('e','epe')
        if x == 'i':
            palavra.replace('i','ipi')
        if x == 'o':
            palavra.replace('o','opo')
        if x == 'u':
            palavra.replace('u','upu')
    return palavra