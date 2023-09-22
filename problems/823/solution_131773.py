def faltante(L: list) -> int:
    """Dada uma lista com N - 1 números inteiros, sendo N a quantidade de peças
       de um quebra-cabeça completo, retorna o número da peça que está faltando
       no quebra-cabeça

       Parameters:
       L: Lista composta por números inteiros não repetidos com N - 1 peças,
       sendo N a quantidade de peças de um quebra-cabeça completo, de 1 a N

       Return:
       Dado o parâmetro "L", retorna um número inteiro que pertence ao intervalo
       [1, N], mas que não pertence a lista do parâmetro "L"

       Examples:
       faltante([3, 1]) == 2
       faltante([1, 2, 3, 5]) == 4
       faltante([2, 4, 3]) == 1
    """

    list.sort(L)
    N = list(range(L[-1] + 1))
    del N[0]
    i = 0

    if L == N:
        return len(L) + 1
    else:
        while N[i] == L[i]:
            i = i + 1
        return N[i]