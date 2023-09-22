def maiores(inteiros,n):
    '''Dada uma lista de números inteiros e um número inteiro n, retorna outra lista com todos os números da lista original maiores que n, em ordem crescente; list,int -> list'''
    
    if n in inteiros:
        quantidade = list.count(inteiros,n)
        list.append(inteiros,n)
        list.sort(inteiros)

        indice = list.index(inteiros,n)
        lista_final = inteiros[indice + quantidade + 1:]

    else:
        list.append(inteiros,n)
        list.sort(inteiros)

        indice = list.index(inteiros,n)
        lista_final = inteiros[indice + 1:]
        
    return lista_final