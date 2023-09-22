def lingua_p(palavra):
    palavra = str.lower(palavra)
    i = 0
    nova = ''
    while i < len(palavra):
        if palavra[i] in "aeiou":
            nova = nova + ( str(palavra[i])+ 'p' + str(palavra[i]))
        nova = nova + palavra[i]
        i = i + 1
    return nova