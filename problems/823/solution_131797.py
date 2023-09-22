def faltante(listadepecas):
    """Função que dada uma lista com N - 1 inteiros numerados de 1 a N com
       um número aleatório faltando, retorna o número inteiro x que 
       pertence ao intervalo [1,N] mas que está faltando na lista.
       list -> int
       
       Parâmetros:
       listadepecas: lista com N - 1 inteiros numerados de 1 a N.
       
       returns: O número inteiro x que pertence ao intervalo [1,N] mas que
                está faltando na lista.
    """
    contador = 0
    contador2 = 1
    faltante = 0
    while contador < len(listadepecas) and faltante == 0:
        if listadepecas[contador] != contador2:
            faltante += contador2
        contador = contador + 1
        contador2 = contador2 + 1
    return faltante