def filtraMultiplos(lista, n): 
    """Retorna uma lista contendo todos os elementos da lista original que porem divisiveis por n;
       Entrada: list, int;
       Saída: list;
    """
    if lista[1]%n==0:
        return [lista[1]]
    for n in range(len(lista)):
        if lista%n==0:
            return [len(lista)]