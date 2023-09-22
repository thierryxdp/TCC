def carros(pessoas, passageiros=5):
    """Retorna o número de carros necessários para transportar uma determinada quantidade de pessoas que é o primeiro valor de entrada, dado o número de passageiros como o segundo valor de entrada;
      int,int->int"""
return math.ceil(pessoas/passageiros)