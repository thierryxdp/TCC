def maiores(lista:list, n:int)->list:
    """Função que retorna uma lista que contenha todos os numeros da lista original maiores que o numero 'N'."""    
    list.append(lista,n)
    list.sort(lista)
    posicao=list.index(lista,n)+1
    return lista[posicao:]