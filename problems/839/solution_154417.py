def carros(x, y=5):
    """Calcula o numero de veiculos necessários para atender a todos os passageiros dados o numero
    de passageiro e a capacidade do veiculo, se a capacidade não for informada ela é 5;
    int, int -> float"""
    if x==y or x==0 or y==1:
        return x//y
    else:
        return x//y + 1
    
    #teste 1
    #carros (12) == 3
    #teste 2
    #carros (1) == 1
    #teste 3
    #carros (0) == 0