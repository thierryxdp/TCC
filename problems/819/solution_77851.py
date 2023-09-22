def filtraMultiplos (listanumeros:list, n: int)-> list:
    """Função que recebe uma lista de números e um número 
    n, e retorna outra lista contendo todos os elementos 
    da lista original."""
    listanova = []
    i = 0
    while i < len(listanumeros):
        if listanumeros[i] % n == 0:
            return listanova = listanova + listanumeros[i]
        i=i+1
    return listanova