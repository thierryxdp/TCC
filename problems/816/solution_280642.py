def maiores(lista, n):
    """Função que retorna uma lista dos maiores numeros n de uma lista de numeros e um numero n
    list, int -> list"""
    maiores_que_n = [numero for numero in lista if numero > n]
    list.sort(maiores_que_n)
    return maiores_que_n