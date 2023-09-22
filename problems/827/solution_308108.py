def qtd_divisores(numero):
    """Recebe um número inteiro e retorna quantos divisores
inteiros positivos esse número tem.
int -> int
"""
    ls_atual = []
    if numero<0:
        return 0
    for i in range(1,numero+1):
        if numero%i == 0:
            list.append(ls_atual, i)
    return len(ls_atual)