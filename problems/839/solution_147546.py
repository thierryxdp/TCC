from math import ceil 
def carros(pessoas,vagas=5):
    ''' Retorna o numero de veiculos necessarios para transportar um determinado
    numero de pessoas (dado como entrada), considerando que cada veiculo tenha 
    a mesma capacidade fixa de vagas (tambem dado como entrada, mas a funcao 
    considera 5 vagas por veiculo como valor default)'''
    return math.ceil(pessoas/vagas)