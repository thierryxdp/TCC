def filtraMultiplos(lista, numero):
    """"""Função que filtra os múltiplos de um nº n.Deve receber como entrada 
    uma lista de nºs e um nº,e retornar outra lista contendo todos os 
    elementos da lista original que forem divisíveis por n;
    list, int -> list"""
    """
    i = 0
    novaLista = []
    while i < len(lista):
        if lista[i] % numero == 0:
            novaLista.append(lista[i])

        i += 1

    return novaLista