def faltante(x):
    pecas = len(x)+ 1
    total = [*range(1, pecas + 1)]
  
    for item in total:
      if item not in x:
        pecafaltando = item
    return pecafaltando