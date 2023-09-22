def lingua_p(palavra):
    indice = 0
    nova_palavra= palavra
    while (indice < len(palavra)):
        if  (str.lower(palavra[indice]) in 'aeiou'):
            nova_palavra[indice+1:indice+1] = 'p'
            nova_palavra[indice+2:indice+2] = palavra[indice]
    return nova_palavra