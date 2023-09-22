def carros(pessoas,capacidade=5):
    """calcula quantos carros sao necessarios para se fazer uma viagem atraves do numero de pessoas e da capacidade de cada carro"""
    qtd=pessoas/capacidade
    if qtd%1==0:
        return qtd
    else:
        return (qtd//1)+1