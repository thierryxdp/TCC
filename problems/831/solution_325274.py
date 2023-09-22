def lingua_p(palavra):
    for c in palavra:
        i=palavra.index(c)
       	if i in 'aeiou':
           	palavra=palavra[i]+'p'+palavra[i:]
        return palavra