def lingua_p(palavra):
    indice = 0
    nova_palavra=''
    while (indice < len(palavra)):
        if  (str.lower(palavra[indice]) in 'aeiou'):
            palavra = palavra[0:indice+1] +'p'+palavra[indice:]
        indice += 1
    return palavra