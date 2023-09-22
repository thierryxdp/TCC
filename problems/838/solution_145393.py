def bombom(dinheiro_total, preco):
    '''a funcao retorna a quantidade de bombons comprada, dados o dinheiro
    total e o preco'''
    
# parametros: dinheiro_total -> dinheiro que Joaozinho possui
#             preco          -> preco de um bombom

  return math.floor(dinheiro_total/preco), dinheiro_total - math.floor(dinheiro_total/preco) * preco

# Se tenho 30.00 reais e o bombom custa 5.00 reais 
# entao posso comprar 6 bombons
print bombom(30, 5)
print "\n"