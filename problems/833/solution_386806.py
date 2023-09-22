def conta_numero(n, M):
    """Recebe um número inteiro e uma matriz de inteiros.
Retorna quantas vezes o número inserido ocorre dentro da
matriz.
int, mat -> int
"""    
    contador = 0
    for linhas in M:
        for colunas in linhas:
            if colunas == n:
               	contador += 1
    return contador