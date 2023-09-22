def carros(P,C=5):
   """Função que calcula o numero de veiculos necessarios, 
   com a capacidade C para transportar o numero de pessoas P"""
   if P//C < P/C:
        return (P//C+1)
     else:
        return (P//C)