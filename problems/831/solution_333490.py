def lingua_p(palavra):
    for x in palavra:
        if x in 'aeiou':
            palavrap = palavra.replace(x,x+'p'+x)
            return(palavrap)