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
    contador = 1
    while contador < len(listadepecas) + 1:
        if listadepecas[contador] == contador:
            contador = contador + 1
        else:
            return contador