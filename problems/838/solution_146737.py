def num_bombons(dinheiro,preco):
    if dinheiro == preco:
        return dinheiro/preco
    elif dinheiro > preco:
        return "1 ou mais bombons"
    else:
        return "nenhum bombom"