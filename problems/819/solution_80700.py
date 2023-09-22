def multiplos(ListaNumeros, N):
    '''Funcao que, recebendo como entrada uma lista de numeros e um outro
valor numerico N, retorna outra lista contendo os elementos da lista original que
forem multiplos de N.
List, int -> List'''
    Proximo = 0
    ListaMultiplos = []
    while Proximo < len(ListaNumeros):
        if ListaNumeros[Proximo]%N == 0:
            ListaMultiplos = ListaMultiplos + [ListaNumeros[Proximo],]
        Proximo = Proximo + 1
    return ListaMultiplos