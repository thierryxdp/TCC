def posLetra(f, p, i):
    """Função que recebe uma string (f), uma letra 
    (p) e um número (i), e retorna o indice da ijezima
    ocorrência da letra p em f
    str, str, int -> int"""
    if f.count(p)<i:
        return -1
    contador = 0
    extencao = len(f)
    atual = 0
    contQtd = 0
    while contador < extencao and contQtd < i:
        if f[contador] == p:
            atual = contador
            contQtd += 1
        contador += 1
    return atual