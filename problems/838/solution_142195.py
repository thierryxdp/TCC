def num_bombons(x):
    """ Função que calcula a 
        quantitidade de bombons que ele consegue comprar
        Entrada: FLOAT,INT
        SAIDA:INT"""
    preco_bombons = float(2.50)
    quant = int(input("DIGITE A QUANTIDADE DE BOMBONS DESEJADA: "))
    calculo = preco_bombons*x
    return(calculo)