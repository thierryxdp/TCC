def maiores(lista,n):
    '''funçao que retorna uma lista com numeros em ordem crescente maiores que o numero de entrada''' 
    '''list,int->list''' 
    list.append(lista,n)
    list.sort(lista)
    i=list.index(lista,n)
    return lista[i+1:]