def qtd_divisores(numero):
    """A entrada será um número, que está no
    parâmetro e o retorno será a quantidade
    de números de divisores o número original
    possui."""
    #num -> num
    contador = 0
    i = 0
    while list(range(1, +1)) in i:
             if numero % i == 0:
                contador + 1
    return contador