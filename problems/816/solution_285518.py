def maior_que(elemento,valor_limite):
    if(elemento > valor_limite):
        return True
    else:
        return False
    return False
def maiores(lista,n):
    '''
        Funçao que dada uma lista de numeros inteiros e um numero inteiro n, retorna
        outra lista, que contenha todos os numeros da lista original maiores que n
        ordenados em ordem crescente
        lista = list.
        n = int.
        return = list.
    '''
    resultado = filter(lambda elemento: maior_que(elemento,n),lista)
    return sorted(list(resultado))