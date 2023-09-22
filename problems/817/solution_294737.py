def acima_da_media(lista_notas):
    """função que retorna uma lista com as notas dos alunos que ficaram acima da média,
    através da lista de entrada 'lista_notas';
    Entrada = list
    Saída = list"""
    m = sum(lista_notas)/len(lista_notas)
    
    if m not in lista_notas:
        list.append(lista_notas,m)
    	list.sort(lista_notas)
    	x = list.index(lista_notas,m)
    	y = lista_notas[x+1:]
   		return y
    else:
        list.sort(lista_notas)
        lista_notas[m:]