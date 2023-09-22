from math import ceil
def carros(n,v=5):
    '''Função que, dados o número de passageiros e a 
    capacidade de transporte do veículo, retorna a quantidade
    de veículos necessários para a viagem'''
    '''a função conta com um default no número de vagas no carro, para carros convencionais'''
    '''int,int --> int'''
    
    return ceil(n/v)