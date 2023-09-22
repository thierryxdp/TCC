'''eu recebo uma lista de numeros interios e um numero 
inteiro n. Meu retorno deve ser uma lista que contenha 
APENAS os numeros da lista original maiores que n em 
ordem crescente.
Organizando o raciocínio da questao: 1) eu recebo uma lista 
em uma ordem qualquer e um numero n a ser adicionado nessa 
lista (igual a questao anterior);
2) por isso, preciso primeiramente criar uma nova lista 
com a lista inicial adicionada do numero n;
3) a partir disso, uso a funcao list.sort para ordenar em 
ordem crescente;
4) em seguida, como quero uma nova lista apenas com os 
numeros maiores que n, preciso descobrir o indice do 
elemento n nessa lista ordenada
5) e usa-lo para fatiar essa lista, gerando uma nova apenas 
com os numeros maiores que n. Nesse caso, devo adicionar 1 
ao indice de n, pois n não pode estar incluso na lista 
de retorno'''

def maiores(lista_numeros,n):
    '''Funcao que recebe de entrada uma lista de numeros 
    inteiros e um numero inteiro n e retorna outra lista 
    com todos os numeros da lista original
    maiores que n em ordem crescente.
    list, int -> list'''
    lista_maiores = lista_numeros + [n]
    if n in lista_numeros:
        lista_maiores = lista_numeros
    list.sort(lista_maiores)
    return lista_maiores[list.index(lista_maiores,n)+1:]

#casos de teste
#maiores([0,2,3,4,5,6],10) == []
#maiores([21,34,15,12],8) == [12, 15, 21, 34]
#maiores([21,2,2,2,4,11],3) == [4, 11, 21]
#maiores([2,3,6,5,4],4) == [5, 6]