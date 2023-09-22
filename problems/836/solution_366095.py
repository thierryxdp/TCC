def busca(setor,matriz):
  '''Dado um setor e uma matriz com os dados dos funcionarios, retorna todos funcionarios que são do setor dito.
   str, matriz -> matriz'''
  soma = []
  for x in range(len(matriz)):
   if setor in matriz[x]:
     soma = soma + matriz[x]
  return [soma]