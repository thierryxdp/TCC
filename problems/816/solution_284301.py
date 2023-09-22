def maiores(lista_inteiros, n):
    """
    Essa função recebe uma lista de números inteiros e um número inteiro n
    assim ela retorna uma lista dos números maiores que n (o número inteiro)
    em ordem crescente;
    list, int -> list
    """
    resultado = []
    for i in range(len(lista_inteiros)):
        if lista_inteiros[i] > n:
            resultado.append(lista_inteiros[i])
    resultado.sort()
    return resultado