def maiores(lista_num, n):
    '''retorna todos os numeros maiores que n(num informado pelo usuário)'''
    lista = [n]
    list_compl = lista_num + lista
    list.sort (lista_compl)
    elementos=len(list_compl)
    xmax= n
    for list_compl[x] in range (1,elementos+1):
    	if list_compl[x] > n:
        	list_maior = list_maior + list_compl[x]
    return list_maior