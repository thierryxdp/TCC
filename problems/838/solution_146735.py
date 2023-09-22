def num_bombons(dinheiro,preco):
    if dinheiro == preco:
        return "1 bombom"
    elif dinheiro > preco:
        return "mais de 1 bombom"
    else:
        return "não é possível comprar"