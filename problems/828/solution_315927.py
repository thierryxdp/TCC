def primo(n):
    """Retorna se um número é primo ou não.
    Entrada: int
    Saída: bool
    """
    a = qtd_divisores(n)
    if a == 2:
        return True
    else:
        return False
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