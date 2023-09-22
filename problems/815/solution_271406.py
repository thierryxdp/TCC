def insere(lista_numero,n):
    """Retorna uma nova lista baseada em uma lista de números em ordem crescente
    dada como entrada, incluindo-se um novo número na posição correta (ordenada).
list, int -> list"""
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero

#Casos de teste:
# insere([1,2,4,5,6,7,8],3) == [1, 2, 3, 4, 5, 6, 7, 8]
# insere([5,10,20,25,30],15) == [5, 10, 15, 20, 25, 30]
# insere([100,200,300,400],0) == [0, 100, 200, 300, 400]