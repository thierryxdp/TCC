from math import *
def carros(n_pessoas, cap_veiculo=5):
    '''Calcula a quantidade de veículos necessários,
       dados: o número de pessoas (n_pessoas) e a
       capacidade do veículo (cap_veiculo).
       (Obs: Caso não seja fornecido um valor para a
       capacidade do veículo, será utilizado o convencional 
       de 5 passageiros)
       int, int -> int'''
    return ceil((n_pessoas)/(cap_veiculo))