def carros(pessoas,capacidade=5):
    """calcula a quantidade de carros necessarios para se realizar uma viagem atraves dos numeros de pessoas e capacidade de cada carro"""
    qtd=pessoas/capacidade
    if qtd%10==0:
        return qtd
    else:
        return (qtd//10)+1