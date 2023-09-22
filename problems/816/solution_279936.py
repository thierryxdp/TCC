def maiores(lista,n):
    '''Função que dada uma lista de numeros inteiros, retorna outra lista,
    que contenha todos os números da antiga. lista,int->str'''
    if n not in lista:
        list.append(lista,n)
        
    list.sort(lista)
    ind = list.index(lista,n)
    fatia = lista[ind+1:]
    
    return fatia