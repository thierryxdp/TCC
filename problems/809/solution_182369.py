def intercala(lista1, lista2):
    """Funcao que dada duas lista retorna uma terceira lista"""
list1 = [1, 3, 5] 
list2 = [2, 4, 6] 
print ("Original list1 : " + str(list1)) 
print ("Original list2 : " + str(list2)) 
res = list1 + list2 
res[::2] = list1 
res[1::2] = list2 
print ("A list intercalada e : " + str(res))