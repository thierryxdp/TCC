def pontos_por_time (lista1,lista2):
	'''list,list->dic'''
    L1=['','',[]]
    L2=['','',[]]
    dicionario={list1[1]:0,list2[2]:0}
    if vitoria_time1:
        dicionario[time1] +=3
    if vitoria_time2:
        dicionario[time2] +=3
   	else empate_time1:
        	dicionario[time1] +=1
    else empate_time2:
        	dicionario[time2] +=1
    elif perda_time1:
        dicionario[time1] +=0
    elif perda_time2:
        dicionario[time2] +=0
   return