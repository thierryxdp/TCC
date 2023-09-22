def faltante(l):
    """Recebe uma lista com N - 1 números inteiros numerados de 1 a N e retorna o número inteiro que falta ao intervalode 1 a N;
    assinatura: list(...) --> int
    Casos de teste:
    faltante([2, 4, 3]) == 1
    faltante([1, 2, 3, 5]) == 4
    faltante([3, 1]) == 2"""
    lista_aux = []
    i = 1
    while i <= (len(l) + 1):
        lista_aux.append(i)
        i += 1
        
    for e in lista_aux:
        if not e in l:
            return e