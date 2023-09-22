# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(compras, produtos):
  i = 0
  soma = 0
  while i < len(compras):
    if compras[i] in produtos:
      soma += produtos[compras[i]]
    i+=1
  return round(soma, 2)