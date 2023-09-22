def qtd_divisores(numero):
    """A entrada será um número, que está no
    parâmetro e o retorno será a quantidade
    de números de divisores o número original
    possui."""
    #num -> num
    contador = 0
   
    for i in range(1, numero +1):
             if numero % i == 0:
                contador += 1
    return contador