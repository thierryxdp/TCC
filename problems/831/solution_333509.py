def lingua_p(palavra):
    l = list(palavra)
    n = len(palavra)
    for x in range(1,n+1):
        if l[x] == 'aeiou':
            palavrap = palavra.replace(x,x+'p'+x)
            return(palavrap)