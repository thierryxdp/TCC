def repetidos(lista):
#Funcao que recebe uma lista de numeros como entrada
    i=1
    repeticoes=0
    while i<len(lista):
        if lista[i]==lista[i-1]:
            repeticoes+=1
        i+=1

    return repeticoes
#retorna o numero de vezes que um elemento da lista é igual ao elemento anterior