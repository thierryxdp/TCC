def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
list1 = [1, 3, 5] 
list2 = [2, 4, 6] 
print ("Original list1 : " + str(list1)) 
print ("Original list2 : " + str(list2)) 
res = list1 + list2 
res[::2] = list1 
res[1::2] = list2 
print ("A list intercalada e : " + str(res))