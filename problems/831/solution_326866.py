def lingua_p(palavra):
    indice = 0
    nova_palavra=''
    while (indice < len(palavra)):
        if  (str.lower(palavra[indice]) in 'aeiou'):
            inicio = palavra[1:indice+1]
            fim = palavra[indice:]
            nova_palavra = inicio + 'p' + fim
    return nova_palavra