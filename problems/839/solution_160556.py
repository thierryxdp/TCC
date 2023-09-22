def carros(pessoas,capacidade=5):
"""calcula o numero de carros em relacao do de pessoas; int,int->int"""
carrosnum = math.ceil(pessoas/capacidade)
return carrosnum