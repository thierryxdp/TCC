def maiores(lista,n):
    """recebe uma lista e um número n inteiro e retorna os números da lista que são maiores do que n em ordem crescente.
    list, int-> list
    Explicação: basta inserir o número na lista, ordená-la, descobrir a posição de n e em seguida receber apenas os que se encontram depois de sua posição."""
    list.insert(lista,0,n)
    list.sort(lista)
    x=list.index(lista,n)
    return lista[x+1:]
#teste 1
# maiores([1,2,3,4,6],5)
# saida esperada: [6]
# teste 2
# maiores([1,5,9,10],2)
# saida esperada: [5,9,10]