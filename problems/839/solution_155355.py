from math import ceil

def carros(p,v=5):
    '''Função que calcula a quantidade a quantidade exata de carros/veículos necessários
       para uma viagem, dado o número de passageiros (p) totais nesta viagem.
       ATENÇÃO: Caso o seu veículo tenha capacidade diferente de 5 lugares, informe no espaço reservado 'v'.
       int, int -> int'''
    return ceil(p/v);