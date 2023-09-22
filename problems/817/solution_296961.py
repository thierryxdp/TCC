def maiores(lista, n):
    """tendo como parâmetros uma lista de números inteiros e um número inteiro, a função retorna outra lista, apenas com
    os elementos maiores que n. A lista retornada será em ordem crescente. Para isso, faz-se uma
    lista ''listanova'' que é composta da lista original mais o elemento novo. Então através do list.sort se
    ordenada essa lista e usa-se o list.index para saber o index de n, chamado indexn por conveniência, 
    nessa nova listanova em ordem crescente. Então, como está em ordem crescente, todos os números com index
    maior que o n será automaticamente maior que ele, logo a função retorna a listanova com index [indexn+1]. Caso
    Porém, caso n esteja dentro a lista o numero com o index acima dele possuirá o mesmo valor que o próprio n, por isso,
    a função possui um if que, nesse caso, retorna os indices da listanova apenas após todos os valores acima de n; 
    list, int -> list"""
    listanova = lista + [n]
    list.sort (listanova)
    indexn = list.index(listanova, n)
    if n in lista:
    	return listanova[list.index(listanova,n)+list.count(listanova,n)::]
    else:
    	return listanova[indexn + 1::]
def acima_da_media (lista):
    """tendo como parametros uma lista possuindo as notas de todos os alunos de uma turma, a função
    retorna outra lista, em ordem crescente, com as notas acima da média. Para isso, a função faz média
    dos elementos da lista, então cria uma nova lista apenas com elementos maiores que a média usando a função
    maiores escrita encima. ;list -> list"""
    media = sum(lista)/len(lista)
    listaordenada = maiores (lista, media)
    if len(lista) == 1:
        return []
    else:
		return listaordenada