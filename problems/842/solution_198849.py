def pontos_por_time(lista1, lista2):
	'''list,list->dic'''
    L1=lista1
    L2=lista2
    L1=['','',[]]
    L2=['','',[]]
    
    dicionario={'list1':0,'list2':0}
    if vitoria_time1:
        dicionario[time1] +=3
    if vitoria_time2:
        dicionario[time2] +=3
   	if empate_time1:
        	dicionario[time1] +=1
    if empate_time2:
        	dicionario[time2] +=1
    if perda_time1:
        dicionario[time1] +=0
    if perda_time2:
        dicionario[time2] +=0
   return