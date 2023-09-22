def qtd_divisores(n):
    """Função que ao receber um número inteiro, retorna quantos
    divisores esse número tem;
    int -> int"""
    lista = []
    if n < 0:
        return 0
    for num in range(1,n):
        if n%num == 0:
            list.append(lista,num)
    return len(lista)+1