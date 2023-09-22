def faltante(x):
    '''peg'''
    pecas = len(x)+ 1
    total = [*range(1, pecas + 1)]
    pecafaltando = []
    for item in total:
      if item not in x:
        pecafaltando.append(item)
    return pecafaltando[0]

faltante([[2]])