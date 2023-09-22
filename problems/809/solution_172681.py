#Questão 3
def intercala(lista1,lista2):
    """dada duas listas L1 e L2 de tamanho 3,
gera uma lista 3 que é formada intercalando elementos
de L1 e L2; ex: >>>intercala([1,3,5],[2,4,6])
= [1, 2, 3, 4, 5, 6]  | int,int -> int"""
    #Colchetes usados para trasnformar os int em lista e
    #assim poder concatenar 

    return [lista1[0]]+[lista2[0]]+[lista1[1]]+[lista2[1]]+[lista1[2]]+[lista2[2]]