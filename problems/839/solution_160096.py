def carros(pessoas,capacidade=5):
    """Calcula o valor de carros necessários para viagem dado o número total de pessoas e a capacidade dos carros (caso não informado, o valor padrão adotado para a capacidade dos carros é de 5 pessoas"""
    if pessoas%capacidade==0:
        return pessoas/capacidade
    else:
        return pessoas//capacidade+1