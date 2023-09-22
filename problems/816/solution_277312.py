def maiores(lista,n):
    '''Função que dada uma lista de números inteiros e um número inteiro n '''
    '''Retorna outra lista, que contenha todos os números da lista original maiores que n '''
    '''list, int -> list '''
     for c in lista:
            if c >= n:
                maiores_numeros.append(c)
                return maiores_numeros