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
def primo(numero):
    """Recebe um número inteiro positivo e retorna True
caso esse número seja primo ou False caso contrário.
int -> bool
"""
	if qtd_divisores(numero) == 2:
        return True
    else:
        return False