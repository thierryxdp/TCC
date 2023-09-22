def carros(pessoas,veiculo=5):
    divisao=pessoas/veiculo
    if divisao == round(divisao):
        return divisao
    else:
        return round(divisao+0.5)