def qtd_dividores(numero):
"""Funcao que conte quantos divisores um numero tem;int->int"""
soma=0
lista=list(range(1,numero))
for i in lista:
    if numero%i==0:
        soma=soma+i
 return soma