def soma_h(n):
    """Função que recebe um valor número inteiro n de entrada e retorna o
       valor de H com duas casas decimais.
       int -> int
       
       Parâmtros:
       n: número de termos do somatório de H.
       
       returns: O valor de H com somente duas casas decimais
    """
    valorH = 0
    for termos in range(1,n+1):
        valorH += 1/termos
    return round(valorH,2)