def uppCons(frase):
    a=""
    for i in frase:
        if i not in 'aeiou':
            a+= str.upper(i)
        else:
             if i in 'aeiou':
                 a+= i
             else:
                if i in 'AEIOU':
                    a+= i
    return a