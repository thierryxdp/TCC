#Função que retorna o numero de bombons que Pedrinho pode comprar, após informado dinheiro e preço de um bombom
# float, Float -> int
def num_bombons(din, preco):
    return round((din/preco) - 0.5)