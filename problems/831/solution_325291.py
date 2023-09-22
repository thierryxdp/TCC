def lingua_p(palavra):
    for i in range(0, len(palavra)):
        if palavra[i] in 'aeiouAEIOU':
            letras = str.partition(palavra, palavra[i])
            list.insert(letras, letras[1] ,'p'+ letras[i])
 		return letras