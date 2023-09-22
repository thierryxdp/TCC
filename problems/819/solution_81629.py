def filtraMultiplos(lista_num,num):
    '''Função que recebe como entrada uma lista de números e 
    um número n, e retorna outra lista contendo todos os elementos
    da lista original divisiveis por n. list, int->list'''
    i=0
    lista_final=[]
    while i<len(lista_num):
    	if lista_num[i]%num==0:
            list.append(lista_final,lista_num[1])
        i+=1
    return lista_final