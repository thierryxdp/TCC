def viagem_carro(p,v=5):
    """ funcao que dado o numero de pessoas(p) e numero de vagas por carro (v), retornara a quantidade maxima de pessoas por carro.
    int,int -> int """
    return importmath.ceil (p/v)