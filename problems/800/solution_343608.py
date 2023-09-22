def total( lista_compras, produtos):
    """ Função que calculo o valor de uma lista de 
    compras.
    Entrada: list, dicionário
    Saída: float """ 
    
    custo = 0
    for compra in lista_compras:
        preco = produtos[compra]
        custo += preco
    return round(custo,2)