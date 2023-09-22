def maiores(lista,n):
    '''
    	Função que recebe como entrada
        uma lista com números inteiros
        e um número inteiro n, e retorna 
        essa lista apenas com os números 
        maiores que n, na ordem crescente
        : param lista: list
        : param n: int
        : return: list
    '''
    list.append(lista,n)
    list.sort(lista)
    indice = list.index(lista,n)
    lista = lista[indice:]
    qtd_n_aparece = list.count(lista,n)
    del lista[0:qtd_n_aparece]
    return lista