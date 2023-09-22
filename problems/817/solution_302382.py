def maiores(lista_numero,n):
  lista_ord = []
  list.append(lista_numero,n)
  list.sort(lista_numero)
  ind = list.index(lista_numero,n)
  lista_ord += lista_numero[(ind+1):]
  return lista_ord

def acima_da_media(notas):
  '''Função que, dada uma lista com as notas dos alunos de uma turma, retorna uma lista ordenada com as notas que ficaram acima da média.
  list -> list'''

  if len(notas) == 1:
    return []
  
  else:
    media = sum(notas) / len(notas)
    return maiores(notas,media)