def carros(P,C=5):
   """Função que calcula o numero de veiculos necessarios, 
   com a capacidade C para transportar o numero de pessoas P"""
   return int(round(P/C+0.5))