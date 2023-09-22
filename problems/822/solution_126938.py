def repetidos(listanumeros:list):
    i=0
    contador=0
    #Verifica enquanto I for menor que o tamanho da lista
    while i<len(listanumeros):
        #Verifica se o próximo número é igual ao atual
        if listanumeros[i-1]==listanumeros[i]:
            contador +=1
        i+=1
    return contador