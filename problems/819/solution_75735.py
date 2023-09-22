def filtraMultiplos(lista, n): 
    """Retorna uma lista contendo todos os elementos da lista original que porem divisiveis por n;
       Entrada: list, int;
       Saída: list;
    """
    if lista[1]%n==0:
        return [lista[1]]