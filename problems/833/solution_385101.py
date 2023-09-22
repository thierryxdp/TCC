# Dado um número e uma matriz, retorna quantas
# vezes o número aparece na matriz.
# Resolução:
# 1. Para cada linha, contar quantas vezes o número aparece:
# 1.1 Para cada elemento da lista que forma a matriz;
# 2. Acumula as ocorrências de todas as linhas;
# 3. Devolve

def conta_numero(numero: int, matriz: list) -> int:
    '''Dado um número e uma matriz, retorna quantas
    vezes o número aparece na matriz'''
    ocorrencia = 0
    for linha in matriz:
        ocorrencia += list.count(linha, numero)
    return ocorrencia