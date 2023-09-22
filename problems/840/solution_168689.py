def bolos(A,B,C)
"""Função que define a quantidade de ingredientes necessários para retornar a quantidade de bolos possiveis de se fazer com os ingredientes dados"""
return min((A//2),(B//3),(C//5))