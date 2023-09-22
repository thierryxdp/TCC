def num_bombons(dinheiro, preco):
    """Dados quantidade de dinheiro e preço dos bombons, retorna o número de bombons que Pedrinho consegue comprar
    float, float -> int"""
    x = dinheiro
    y = preco
    return (x - x%y)/y