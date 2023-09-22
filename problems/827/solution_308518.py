def qtd_divisores(numero):
    """A função recebe um número inteiro e retorna a quantidade
    de divisores (outro int) desse número."""
    lista = list(range(numero+1))
    contador = 0
    for elemento in lista:
        if numero % elemento == 0:
            contador += 1
    return contador