def num_bombons(dinheiro,preco):
    if dinheiro == preco:
        return "1 bombom"
    elif dinheiro > preco:
        return "1 ou mais bombons"
    else:
        return "nenhum bombom"