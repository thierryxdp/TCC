def repetidos(lista):
    """Funcao que recebe uma lista de numeros de entrada e retorna o numero de vezes
    que o elemento da lista e igual ao anterior;
    list -> int"""
    contador=1
    acumulador=[]
    while contador<len(lista):
        if lista[contador]==lista[(contador)-1]:
            acumulador+=[1]
        contador+=1
    return sum(acumulador)