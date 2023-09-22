def repetidos (listaNum):
    "função que recebe uma lista, e retorna o número de vezes que um elemento da lista é igual ao anterior.list->int."
    i=0
    soma = 0
    while i < len(listaNum)-1:
        if listaNum[i] == listaNum[i+1]:
            soma = soma +1
        i = i+1
    return soma