def lingua_p(palavra):
    palavra = str.lower(palavra)
    i = 0
    nova = ()
    while i < len(palavra):
        if palavra[i] in "aeiou":
            (palavra[i],) = (str(palavra[i])+str('p')+str(palavra[i]))
        nova = nova + (palavra[i])
        i = i + 1
    return nova