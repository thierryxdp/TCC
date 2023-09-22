def bolo (a,b,c):
"""função que calcula quantos bolos são possíveis fazer com um número determinado de ingredientes"""
return min(a//2,b//3, int(c/5))