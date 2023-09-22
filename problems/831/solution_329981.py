def substituir(string):
  ultimo = None
  for atual in string:
    if atual == ultimo:
      yield 'x'
    yield atual
    ultimo = atual

s = "pizza carro passaro"
print(''.join(substituir(s)))