def repetidos(lista):
    #cria o indice i
    i=0
    #cria a variavel de saida a
    a=0
    #repete a funçao do indice 0 ao len(letra)-1
    while i<len(lista)-1:
        #se as letras de indice i e i+1 forem iguais
        if lista[i]==lista[i+1]:
            #soma um valor a saida a
            a+=1
        #adiciona 1 ao indice
        i+=1

    return a