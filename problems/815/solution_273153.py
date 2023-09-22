def insere(lista_numero,n):
    """essa função serve para inserir um número em uma lista na ordem crescente
    list,int->list"""
    lista_numero.append(n)
    list.sort(lista_numero)
    return lista_numero

   #casos de teste
   #insere([1,2,3,4,5],3) == [1, 2, 3, 3, 4, 5]
   #insere([6,7,8,9,10],17) == [6, 7, 8, 9, 10, 17]
   #insere([11, 12, 13, 15, 16], 10) == [10, 11, 12, 13, 15, 16]