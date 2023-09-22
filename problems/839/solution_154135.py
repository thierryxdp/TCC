import math

def carros (pessoas:int, vagas:int=5) ->float :
   '''coloque o número de pessoas que vão na viagem'''
   return math.ceil(pessoas/vagas)