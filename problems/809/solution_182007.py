def intercala(lista1,lista2):
    """intercala duas listas"""
    test_list1 = [1, 4, 5] 
test_list2 = [3, 8, 9] 
print ("Original list 1 : " + str(test_list1)) 
print ("Original list 2 : " + str(test_list2)) 
res = test_list1 + test_list2 
res[::2] = test_list1 
res[1::2] = test_list2 
print ("The interleaved list is : " + str(res))