def carros (pessoas, capacidade=5):
"""retorna o número de carros necessários em relacao ao numero de pessoas dividindo o pessoas por carros a princio de capacidade 5; int,int -> int"""
carrosnum = math.ceil(pessoas/capacidade)
return carrosnum