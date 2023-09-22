def num_bombons(d,v):
    """Calcula a quantidade de bombons que podem ser comprados , realizando
    a divisão do valor do bombom com o valo em real inserido; float,float ==> int """
    quantidade = d/v
    return math.floor(quantidade)