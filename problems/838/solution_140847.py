def max_bombons(d, p):
    """
    Descrição: Recebe o montante e o preço de cada bombom, e retorna o 
    numero de bombons que é possível comprar com o montante informado

    Parâmetros:
        d, p -> float
        Quantidade de dinheiro que se tem e preço de um bombom

    Retorno:
        Número de bombons possível de se comprar -> int
    """
    n = d/p
    return int(n)