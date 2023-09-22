# Dado um número, queremos sua quantidade de divisores.
# Resolução:
# 1. Verifica, para todo número i inteiro em [1, numero],
#    se o resto da divisão de numero por i é zero;
# 2. Caso seja, adiciona-o à lista de divisores do número;
# 3. Verifica quantos elementos a lista possui;
# 4. Devolve

def qtd_divisores(numero: int) -> int:
    '''Devolve a quantidade de divisores de um número'''
    divisores = list()
    for num in range(1, n + 1):
        if (numero % num == 0):
            list.append(divisores, num)
    quantidade = len(divisores)
    return quantidade