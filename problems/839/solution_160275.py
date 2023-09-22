from math import *

def carros(pessoas,veiculo=5):
 '''Função que calcula quantidade exata de carros necessários para uma viagem;int,int-->int'''
 return ceil(pessoas/veiculo)