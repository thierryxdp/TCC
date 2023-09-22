def lingua_p(palavra):
    indice = 0
    nova_palavra=''
    while (indice < len(palavra)):
        if  (str.lower(palavra[indice]) in 'aeiou'):
            nova_palavra = palavra[0:indice+1] +'p'+palavra[indice:]
    return nova_palavra