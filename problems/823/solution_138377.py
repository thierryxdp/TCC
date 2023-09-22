def faltante(piece_list):
  """dada uma lista com n-1 inteiros numerados de 1 a n, retorna o numero inteiro que ta faltando
    list->int"""
  last_number = len(piece_list) + 1
  piece_list.sort()