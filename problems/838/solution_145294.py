def num_bombons(money,preço):
    """Calcula a quantidade de bombons que podem ser comprados , realizando
    a divisão do valor do bombom com o valo em real inserido; float,float ==> int """
    quant= money/preço
    round(quant)
    return quant