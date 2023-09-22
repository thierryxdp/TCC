def qtd_divisores(numero):
    """A função recebe um número inteiro e retorna a quantidade
    de divisores (outro int) desse número."""
    if numero < 0:
        return 0
    else:
        lista = list(range(numero+1))
        del(lista[0])
        contador = 0
        for elemento in lista:
            if numero % elemento == 0:
                contador += 1
        return contador