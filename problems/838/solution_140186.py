def'num_bombons'(dinheiro_total, preco):
  return math.floor(dinheiro_total/preco), dinheiro_total - math.floor(dinheiro_total/preco) * preco

# Se tenho 30.00 reais e o bombom custa 0.70 centavos
# entao posso comprar 42 bombons
Entrada [30,0.70]