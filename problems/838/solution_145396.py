def bombom(dinheiro_total, preco):
    '''a funcao retorna a quantidade de bombons comprada, dados o dinheiro
    total e o preco'''
#se o bombom custa R$5 e o dinheiro é R$30, pode-se comprar 6 bombons
return math.floor(dinheiro_total/preco)
print bombom(30, 5)
print "\n"