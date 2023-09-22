def maiores (listanumeros,n):
    """Função que dado uma lista de úmeros inteiros e um número inteiro n,
       retorna outra lista(novalista), que contenham todos os números da lista
       original maiores que n.
       list,int->list
       
       Parâmetros:
       listanumeros: Lista com uma série de números inteiros que irá gerar 
                     a nova lista.
       n: É um inteiro que servirá para comparar com os demais termos da lista.
       
       returns: Outra lista que contem todos os números da lista original maiores que n
    """
    novalista = []
    i = 0
    while i  < len(listanumeros):
        if listanumeros[i]>n:
            novalista = novalista + [listanumeros[i],]
            i = i + 1
    return sorted(novalista)