def repetidos(lista):
    '''A partir da lista retorna a quantidade de numeros
    que sao iguais ao anterior na lista
    list -> int'''
    k=1
    repeticoes = []
    while k < len(lista):
        if lista[k] == lista[(k-1)]:
            list.append(repeticoes,lista[k])
        k +=1
    return len(repeticoes)