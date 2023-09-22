def carros(pessoas,veiculo=5):
    divisao=pessoas/veiculos
    if divisao == round(divisao):
        return divisao
    else:
        return round(divisao+0.5)