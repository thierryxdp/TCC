def total(ls, tabela):
  custo = 0
  for p in ls:
    custo += dict.get(tabela, p, 0)
  return custo