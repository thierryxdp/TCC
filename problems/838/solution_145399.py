# parametros: dinheiro_total -> dinheiro que Joaozinho possui
#             preco          -> preco unitario de um bombom
#
# a funcao retorna a quantidade de bombons comprada e o troco
def bombom(dinheiro_total, preco):
    '''funçao que calcula quantos bombons podemos comprar e o troco'''
  return math.floor(dinheiro_total/preco), dinheiro_total - math.floor(dinheiro_total/preco) * preco

# Se tenho 30.00 reais e o bombom custa 0.70 centavos
# entao posso comprar 42 bombons e sobram 0.60 centavos
print bombom(30, 0.70)
print "\n"