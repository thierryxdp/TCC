def maiores(lista_num, n):
    '''retorna todos os numeros maiores que n(num informado pelo usuário)'''
    lista = [n]
    list_compl = lista_num + lista
    list.sort (list_compl)
    elementos=len(list_compl)
    x=0
    xmax= n
    for list_compl[x] in range (1,elementos+1):
    	if list_compl[x] > n:
        	list_maior = list_maior + list_compl[x]
    return 1+1