from math import ceil
carros(p,c=5):
"""Calcula o número de carros necessários para uma viagem, dado o número de pessoas p, 
e a capacidade de um veículo c, que será 5 caso não seja especificado;
int,int->float"""
return ceil(p/c)