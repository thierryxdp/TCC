def repetidos(lista):
    "Função que dada uma lista númerica, retorna o número de vezes que há numeros que são iguais aos seus antecessores. list --> int"
    nreps=0
    i=1
    while i< len(lista):
        if lista[i]==lista[i-1]:
            nreps=nreps+1
        i=i+1
    return nreps