def bolo (a, b, c):
"""calcula a quantidade de bolos que pode ser feito com a quantidade de ingredientes dada
entrada= int, int, int
saida=int
"""
qtd_farinha=a//2
qtd_ovo=b//3
qtd_leite=c//5
return min(a//2, b//3, c//5)