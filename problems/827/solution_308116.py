def qtd_divisores(numero):
    """A entrada será um número, que está no
    parâmetro e o retorno será a quantidade
    de números de divisores o número original
    possui."""
    #num -> num
    contador = 0
    for divisor in numero:
        if numero // 2:
            return len(numero)