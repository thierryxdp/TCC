def carros(pessoas,vagas=5):
    """ calcula o número de carros necessarios para fazer uma viagem
    em um carro convencional,se o carro não for convencional, basta 
    por o numero de vagas deste carro;int,int->int"""
    return (pessoas/vagas)%