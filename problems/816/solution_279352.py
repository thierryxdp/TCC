def maiores(intList, n):
    """Recebe uma lista de numeros inteiro e outro número.
    	Retorna outra lista que contém o elementos de intList
        que são maiores que n
        list, int -> list"""
    intList.sort(intList.append(n))
    maiores = intList[intList.index(n)+1:]
    return maiores