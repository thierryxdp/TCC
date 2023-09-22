def find_missing_piece(piece_list):
  """dada uma lista com n-1 inteiros numerados de 1 a n, retorna o numero inteiro que ta faltando
    list->int"""
  last_number = len(piece_list) + 1
  piece_list.sort()

  if piece_list[0] != 1:
    return 1

  for i in range(last_number - 2):
    if piece_list[i] != piece_list[i + 1] - 1:
      return piece_list[i] + 1

  return last_number