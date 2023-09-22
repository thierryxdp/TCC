def filtraMultiplos(lista_num,num):
    '''
    	Função que recebe como entrada uma lista de numeros e um numero
        e retrona outra lista contendo todos os elementos da lista original que 
        forem divisíveis por num.
        i:int.
        lista_num:list.
        num:int.
        return:list
    '''
    lista = []
    i=0
    while i < len(lista_num):
        if lista_num[i]%num == 0:
            lista.append(lista_num[i])
        i+=1
    return lista