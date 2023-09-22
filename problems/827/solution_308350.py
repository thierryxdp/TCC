def qtd_divisores(numero):
    """Função que calcula a quantidade de divisores do numero fornecido
    int -> int"""
    contador = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            contador += 1
    return contador