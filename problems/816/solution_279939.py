def maiores(lista_numeros:list,n:int) -> list:
    """Dados uma lista de números inteiros (lista_numeros)
    e um número inteiro n, a função retorna uma lista com
    todos os números da lista original maiores que n."""
    
    list.append(lista_numeros,n)
    list.sort(lista_numeros)
    posicao_n = list.index(lista_numeros,n)
    lista_maiores_n = lista_numeros[posicao_n+1:]
    
    return lista_maiores_n