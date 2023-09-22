def lingua_p(palavra):
    l = list(palavra)
    v = 'a','e','i','o','u'
    n = len(palavra)
    for x in palavra:
        if l[x] in v:
            palavrap = palavra.replace(x,x+'p'+x)
            return(palavrap)