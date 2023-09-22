def carros(n_pessoas,p=5):
    '''
    Calcula o numero exato de carros necessário
    para transportar n pessoas, sabendo que 
    o carro permite apenas 5 passageiros
    int, int 
    return int
    '''
    return round((n_pessoas//p)+0.5)