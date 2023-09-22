# Dado N, calcula o somatório de 1/i para i=1 até i=N.
# Resolução:
# 1. Para todo número i em [1, N], calcula 1/i;
# 2. Soma todos os valores obtidos em (1);
# 3. Aproxima (2) para que possua 2 casa decimais;
# 4. Devolve

def soma_h(N: int) -> float:
    '''Calcula o somatório de 1/i para i=1 até i=N'''
    soma = 0
    termo = 0
    for i in range(1, N + 1):
        termo = 1 / i
        soma += termo
    H = round(soma, 2)
    return H