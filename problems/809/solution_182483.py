def intercala(list1, list2):
    '''funçao que dadas duas listas L1 e L2 de tamanho 3, gera uma lista L3 que e formada 
    intercalando os elementos de L1 e L2 
    int,list-->list'''
list3 = [list1[0],] + [list2[0],] + [list1[1],] + [list2[1],] + [list1[2],] + [list2[2]]
  	return list3