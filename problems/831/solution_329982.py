def lingua_p(string):
  ultimo = None
  for atual in string:
    if atual == ultimo:
      yield 'x'
    yield atual
    ultimo = atual
    return atual