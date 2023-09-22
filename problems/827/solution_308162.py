def qtd_divisores(numero):
    """A entrada será um número, que está no
    parâmetro e o retorno será a quantidade
    de números de divisores o número original
    possui."""
    #num -> num
    contador = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 28]
   
    for i in range(1, +1):
             if numero % i == 0:
                contador + 1
    return contador