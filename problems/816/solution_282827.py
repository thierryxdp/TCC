def maiores(lista,n):
    '''
    	Função que dada uma lista de inteiros e um numero inteiro 'n', retorna outra lista maiores que 'n', em ordem crescente
        list ->list
    '''
    lista_maior = list.append(lista,n)
    return lista_maior[list.index(lista_maior,n):]        
    #return list.sort(lista_maior)