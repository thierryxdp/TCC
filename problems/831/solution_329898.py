def qtd_divisores(n):

    """Retorna a quantidade de divisores que um número possui.

    Entrada: int

    Saída: int

    """

    lista = []

    contagem = 0

    while contagem < n:

        if n%(contagem + 1)==0:

            list.append(lista, contagem+1)

        contagem += 1

    return len(lista)