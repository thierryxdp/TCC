def num_bombons(preco,dinheiro):
    """ funcao que vai dizer quantos bombom o pedrinho compra
    ao informar quanto de dinheiro tem e o preco do bombom. 
    cabe lembrar que os parametros tem de ser positivos pois 
    nao se pode comprar algo de valor negativo nem comprar uma 
    quantidade negativa de bombom 
    float,float -> int """
    return math.ceil(dinheiro/preco)