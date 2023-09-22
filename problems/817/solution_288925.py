def acima_da_media(lista_numero):
	""" Dada uma lista com as notas dos alunos, retorne uma lista ordenada com as notas que ficaram acima da média""" 
	lista_final = [] 
   	for x in lista_numero:
       		if x>sum(lista_numero)/len(lista_numero):
                	list.append(lista_final, x)
    	
	list.sort(lista_final)     

 	return lista_final