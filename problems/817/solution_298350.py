def maiores(lista,n):
    """ Insira uma lista e um numero inteiro e a funcao ira retornar outra lista contendo todos os numeros 
    da lista original maiores que n, em ordem crescente"""
    maiores = list()
    lista.sort()
    for x in lista:
        if x >= n:
            maiores.append(x)
    return maiores
    
def acima_da_media(notas):
    """ Insira uma lista com as notas dos alunos e a função retornara uma lista ordenada das
    notas acima da media"""
    media = sum(notas)/len(notas)
    acima_media = maiores (notas, media)
    return media