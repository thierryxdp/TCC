def maiores(lista,n):
    '''
    	Função que dada uma lista de inteiros e um numero inteiro 'n', retorna outra lista maiores que 'n', em ordem crescente
        list ->list
    '''
    if n in lista:
        lista_maior = lista[list.index(lista,n):]
        return list.sort(lista_maior)
    else:
        lista_maior = list.append(lista,n)
        lista_maior=lista_maior[list.index(lista_maior,n):]        
        return list.sort(lista_maior)